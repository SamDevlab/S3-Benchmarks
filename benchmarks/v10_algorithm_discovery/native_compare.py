#!/usr/bin/env python3
"""Generate a C/GCC native executable from inferred opaque GF(2) transition columns.

All mathematical fast paths are generic; no case-specific rule is embedded in
the inferred backend. An independent cyclic polynomial routine is a *known*
stronger specialist reference, where applicable. This is a GCC proof-of-concept,
NOT S3 native compiler integration or proof of oracle global linearity.
"""
import json
from pathlib import Path
import statistics
import subprocess
import tempfile

from blackbox_gf2 import infer_gf2_map
from sealed_challenge import cases

HERE = Path(__file__).resolve().parent
C_CODE = r"""
#define _POSIX_C_SOURCE 200809L
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#define WIDTH __WIDTH__
#define HAS_POLY __HAS_POLY__
static const uint64_t BASE[WIDTH] = {__COLUMNS__};
static const uint64_t POLY = __POLY__ULL;
static const uint64_t MASK = (UINT64_MAX >> (64-WIDTH));
static volatile uint64_t sink = 0;

static uint64_t apply(const uint64_t *cols, uint64_t x) {
    uint64_t v = 0;
    while(x) {
        int i = __builtin_ctzll(x);
        v ^= cols[i];
        x &= (x-1);
    }
    return v;
}
static void compose(uint64_t *out, const uint64_t *a, const uint64_t *b) {
    for(int i=0; i<WIDTH; ++i) out[i] = apply(a,b[i]);
}
__attribute__((noinline)) static uint64_t iterative(uint64_t x, uint64_t n) {
    for(uint64_t i=0; i<n; ++i) x=apply(BASE,x);
    return x;
}
__attribute__((noinline)) static uint64_t inferred(uint64_t x, uint64_t n) {
    uint64_t power[WIDTH], temp[WIDTH];
    memcpy(power,BASE,sizeof(power));
    while(n) {
        if(n & 1) x=apply(power,x);
        n >>= 1;
        if(n) {
            compose(temp,power,power);
            memcpy(power,temp,sizeof(power));
        }
    }
    return x;
}
static uint64_t rot(uint64_t x, int k) {
    k %= WIDTH;
    return k ? ((x << k) | (x >> (WIDTH-k))) & MASK : x & MASK;
}
static uint64_t poly_mult(uint64_t a, uint64_t b) {
    uint64_t v=0;
    while(a) {
        int i=__builtin_ctzll(a);
        v ^= rot(b,i);
        a &= (a-1);
    }
    return v;
}
__attribute__((noinline)) static uint64_t specialized(uint64_t x, uint64_t n) {
    uint64_t acc=1, p=POLY;
    while(n) {
        if(n&1) acc=poly_mult(acc,p);
        n>>=1;
        if(n) p=poly_mult(p,p);
    }
    return poly_mult(acc,x);
}
static double now_ns(void) {
    struct timespec t;
    clock_gettime(CLOCK_MONOTONIC_RAW, &t);
    return (double)t.tv_sec * 1000000000.0 + (double)t.tv_nsec;
}
static uint64_t call(int mode, uint64_t x, uint64_t n) {
    return mode==0 ? iterative(x,n) : mode==1 ? inferred(x,n) : specialized(x,n);
}
static double bench(int mode, uint64_t n, int rounds) {
    double xs[31];
    if(rounds < 1 || rounds > 31) exit(2);
    int batch = n < 1000 ? 300 : n < 10000 ? 120 : n < 100000 ? 24 : n < 1000000 ? 5 : 1;
    for(int r=0; r<rounds; ++r) {
        uint64_t v=0;
        for(int warm=0; warm<6; ++warm) v ^= call(mode,((uint64_t)(warm+r+1)*11400714819323198485ULL)&MASK,n);
        sink ^= v;
        double t0=now_ns();
        for(int j=0; j<batch; ++j) {
            uint64_t state=((uint64_t)(j+1+r)*11400714819323198485ULL)&MASK;
            v ^= call(mode,state,n);
        }
        double t1=now_ns();
        sink ^= v;
        xs[r]=(t1-t0)/batch;
    }
    for(int i=1; i<rounds; ++i) {
        double x=xs[i];
        int j=i-1;
        while(j>=0 && xs[j]>x) { xs[j+1]=xs[j];--j; }
        xs[j+1]=x;
    }
    return xs[rounds/2];
}
int main(int argc, char**argv) {
    if(argc!=3) return 2;
    uint64_t n=strtoull(argv[1],NULL,10);
    int rounds=atoi(argv[2]);
    for(int j=0; j<16; ++j) {
        uint64_t x=((uint64_t)(j+1)*11400714819323198485ULL)&MASK;
        uint64_t a=iterative(x,n), b=inferred(x,n);
        if(a!=b) { fprintf(stderr,"DIFFERENTIAL_FAIL n=%llu j=%d\n",(unsigned long long)n,j);return 3; }
        if(HAS_POLY && a!=specialized(x,n)) {
            fprintf(stderr,"SPECIALIST_REFERENCE_FAIL n=%llu j=%d\n",(unsigned long long)n,j);return 4;
        }
    }
    // Interleave order across calls in Python. Each mode gets warmups and medians.
    double a=bench(0,n,rounds);
    double b=bench(1,n,rounds);
    if(HAS_POLY) printf("{\"N\":%llu,\"native_iterative_ns\":%.4f,\"native_inferred_ns\":%.4f,\"native_specialist_ns\":%.4f,\"checksum_valid\":true}\n",
      (unsigned long long)n,a,b,bench(2,n,rounds));
    else printf("{\"N\":%llu,\"native_iterative_ns\":%.4f,\"native_inferred_ns\":%.4f,\"native_specialist_ns\":null,\"checksum_valid\":true}\n",
      (unsigned long long)n,a,b);
    return 0;
}
"""


def emit(challenge, columns):
    if challenge.width > 32:
        raise ValueError("bounded experimental native codegen 1..32")
    text = C_CODE
    for old, new in {
        "__WIDTH__": str(challenge.width),
        "__COLUMNS__": ", ".join(f"{v}ULL" for v in columns),
        "__HAS_POLY__": "1" if challenge.polynomial is not None else "0",
        "__POLY__": str(challenge.polynomial or 0),
    }.items():
        text=text.replace(old,new)
    return text


def run():
    output = []
    with tempfile.TemporaryDirectory(prefix="s3v10_native_") as td:
        tmp = Path(td)
        for c in cases():
            if not c.expected_linear:
                continue
            model = infer_gf2_map(c.step,c.width,probes=128,seed=4051)
            if model.status != "EXHAUSTIVE_ORACLE_EQUIVALENCE" and not model.status.startswith("PROVISIONAL"):
                raise AssertionError("missing certification state")
            code=emit(c,model.columns)
            source=tmp / (c.id+".c")
            executable=tmp / c.id
            source.write_text(code,encoding="utf-8")
            subprocess.run(["gcc","-O3","-std=c11","-Wall","-Wextra",str(source),"-o",str(executable)],check=True,capture_output=True,text=True)
            rows = []
            for n in (100, 1000, 10000, 100000, 1000000):
                run=subprocess.run([str(executable),str(n),"5"],check=True,capture_output=True,text=True)
                row=json.loads(run.stdout.strip())
                row["speedup_direct_over_inferred"] = round(row["native_iterative_ns"]/row["native_inferred_ns"],3)
                if row["native_specialist_ns"] is not None:
                    row["specialist_over_inferred"] = round(row["native_specialist_ns"]/row["native_inferred_ns"],3)
                rows.append(row)
            output.append({
                "case":c.id,"width":c.width,"family":c.family,"oracle_preflight_status":model.status,
                "compiler":"GCC -O3 -std=c11 generated from inferred GF2 transition matrix",
                "result":"NATIVE_DIFFERENTIAL_PARITY_PASS",
                "rows": rows,
            })
            print(c.id,"NATIVE_PASS",
                  "N1M_SPEEDUP",rows[-1]["speedup_direct_over_inferred"],
                  "SPECIALIST_NS",rows[-1]["native_specialist_ns"],flush=True)
    report = {
        "status":"EXPLORATORY_GCC_NATIVE_FROM_BLACKBOX_GF2",
        "backend":"GCC_NATIVE_NOT_S3_NATIVE",
        "blackbox_linearity_proof":False,
        "new_algorithm_claim":False,
        "samples":output,
        "limitations":[
            "Both C iterative and inferred modes use the inferred column representation; specialist reference is provided for cyclic cases.",
            "Single host/session, 5 rounds; very short kernels and nanosecond results can be noisy.",
            "Discovery and compiling costs excluded from warm kernel timings; compare break-even separately.",
            "This proves C code generation for a subset of the inferred GF2 maps, NOT S3 compiler integration.",
            "Probabilistic oracle linearity preflight is not a universal certificate. Do not deploy without source proof.",
        ],
    }
    p=HERE/"native_gcc_results_v10.json"
    p.write_text(json.dumps(report,indent=2),encoding="utf-8")
    print("OUTPUT="+str(p))


if __name__=="__main__":
    run()
