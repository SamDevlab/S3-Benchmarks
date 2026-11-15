/* V10.3: native x86-64 S3 dynamic GF(2) vs independent specialist cyclic C.
 * The shared library is built from S3-generated x86-64 assembly, not C.
 * Harness calls raw compiled exports for timing; the Python public API's
 * certificate verification is intentionally excluded and measured separately.
 * NO security claims / no production promotion from raw timings.
 */
#define _POSIX_C_SOURCE 200809L
#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <time.h>
#include <dlfcn.h>
#include <inttypes.h>

static int W;
static uint64_t MASK;
static volatile uint64_t SINK;
typedef int64_t (*native_s3_t)(int64_t, int64_t);
static native_s3_t S3;

static inline uint64_t rotl(uint64_t x, int k) {
    k %= W;
    return k ? (((x << k) | (x >> (W-k))) & MASK) : (x & MASK);
}

__attribute__((noinline))
static uint64_t direct_rule90(uint64_t state, uint64_t n) {
    for (uint64_t i=0; i<n; ++i) {
        state = (rotl(state,1) ^ rotl(state,W-1)) & MASK;
    }
    return state;
}

static uint64_t cyclic_gf2_multiply(uint64_t a, uint64_t b) {
    uint64_t out=0;
    while (a) {
        int idx=__builtin_ctzll(a);
        out ^= rotl(b,idx);
        a &= a-1;
    }
    return out & MASK;
}

__attribute__((noinline))
static uint64_t specialist_cyclic_power(uint64_t x, uint64_t n) {
    uint64_t p=(UINT64_C(1)<<1) ^ (UINT64_C(1)<<(W-1));
    uint64_t acc=1;
    while (n) {
        if (n&1) acc=cyclic_gf2_multiply(acc,p);
        n >>= 1;
        if (n) p=cyclic_gf2_multiply(p,p);
    }
    return cyclic_gf2_multiply(acc,x);
}

/* Independent generic matrix repeated-squaring backend for algorithm-matched
 * comparison with S3: W columns, branchless GF(2) application, unconditionally
 * compute square each bit-iteration, even on final n==0.
 */
static uint64_t matrix_apply(const uint64_t *columns, uint64_t x) {
    uint64_t result=0;
    for (int i=0;i<W;++i) result ^= columns[i] * ((x >> i)&UINT64_C(1));
    return result;
}
__attribute__((noinline))
static uint64_t generic_gcc_matrix(uint64_t x, uint64_t n) {
    uint64_t columns[32], scratch[32];
    for(int i=0;i<W;++i) {
        uint64_t unit=UINT64_C(1)<<i;
        columns[i]=(rotl(unit,1) ^ rotl(unit,W-1))&MASK;
    }
    while(n) {
        uint64_t applied=matrix_apply(columns,x);
        x=x+(applied-x)*(n&UINT64_C(1));
        n>>=1;
        for(int i=0;i<W;++i) scratch[i]=matrix_apply(columns,columns[i]);
        for(int i=0;i<W;++i) columns[i]=scratch[i];
    }
    return x;
}
static uint64_t call_mode(int mode, uint64_t x, uint64_t n) {
    if (mode==0) return direct_rule90(x,n);
    if (mode==1) return (uint64_t)S3((int64_t)x,(int64_t)n);
    if (mode==2) return specialist_cyclic_power(x,n);
    return generic_gcc_matrix(x,n);
}

static double clock_ns(void) {
    struct timespec t;
    if (clock_gettime(CLOCK_MONOTONIC_RAW,&t)) exit(5);
    return (double)t.tv_sec*1000000000.0+(double)t.tv_nsec;
}

static int choose_batch(int mode, uint64_t n) {
    if (mode==0) {
        if(n>=1000000) return 4;
        if(n>=100000) return 16;
        if(n>=10000) return 100;
        if(n>=1000) return 500;
        return 1200;
    }
    if(mode==1 || mode==3) return 300;
    return 12000;
}

static int compare_double(const void* aa,const void*bb) {
    double a=*(const double*)aa,b=*(const double*)bb;
    return a<b?-1:a>b?1:0;
}

int main(int argc,char **argv) {
    if(argc!=6) {
        fprintf(stderr,"usage: benchmark <so> <width> <N> <rounds> <seed>\n");
        return 2;
    }
    const char *path=argv[1];
    W=atoi(argv[2]);
    uint64_t n=strtoull(argv[3],NULL,10);
    int rounds=atoi(argv[4]);
    uint64_t seed=strtoull(argv[5],NULL,10);
    if(W<2 || W>32 || n > INT64_MAX || rounds<3 || rounds>31) return 3;
    MASK=(UINT64_C(1)<<W)-1;
    void *handle=dlopen(path,RTLD_NOW|RTLD_LOCAL);
    if(!handle) {fprintf(stderr,"dlopen failed: %s\n",dlerror());return 4;}
    *(void**)(&S3)=dlsym(handle,"certified_step_dynamic");
    if(!S3) {fprintf(stderr,"dlsym failed\n");return 5;}

    int checks=0;
    for(int j=0;j<64;++j) {
        uint64_t x=(seed+(uint64_t)j*UINT64_C(11400714819323198485))&MASK;
        uint64_t oracle=direct_rule90(x,n);
        if(oracle!=call_mode(1,x,n) || oracle!=call_mode(2,x,n)
                || oracle!=call_mode(3,x,n)) {
            fprintf(stderr,"DIFFERENTIAL_MISMATCH state=%" PRIu64 " N=%" PRIu64 "\n",x,n);
            return 6;
        }
        ++checks;
    }

    double measurements[4][31];
    for(int round=0;round<rounds;++round) {
        for(int slot=0;slot<4;++slot) {
            int mode=(round+slot)%4;
            int batch=choose_batch(mode,n);
            uint64_t xor_result=0;
            for(int warm=0;warm<8;++warm) {
                uint64_t x=(seed+(uint64_t)(warm+round+1)*UINT64_C(1099511628211))&MASK;
                xor_result ^= call_mode(mode,x,n);
            }
            double start=clock_ns();
            for(int j=0;j<batch;++j) {
                uint64_t x=(seed+(uint64_t)(j+round+1)*UINT64_C(1099511628211))&MASK;
                xor_result ^= call_mode(mode,x,n);
            }
            double stop=clock_ns();
            SINK^=xor_result;
            measurements[mode][round]=(stop-start)/batch;
        }
    }
    double median[4];
    double min[4],max[4];
    for(int mode=0;mode<4;++mode) {
        qsort(measurements[mode],rounds,sizeof(double),compare_double);
        median[mode]=measurements[mode][rounds/2];
        min[mode]=measurements[mode][0];
        max[mode]=measurements[mode][rounds-1];
    }
    printf("{\"width\":%d,\"N\":%" PRIu64 ",\"rounds\":%d,"
           "\"checked_states\":%d,\"parity\":true,"
           "\"median_ns\":{\"iterative_c\":%.4f,\"s3_dynamic_native_raw\":%.4f,\"cyclic_specialist_c\":%.4f,\"generic_matrix_c\":%.4f},"
           "\"ranges_ns\":{\"iterative_c\":[%.4f,%.4f],\"s3_dynamic_native_raw\":[%.4f,%.4f],\"cyclic_specialist_c\":[%.4f,%.4f],\"generic_matrix_c\":[%.4f,%.4f]},"
           "\"checksum_sink\":%" PRIu64 "}\n",
           W,n,rounds,checks,median[0],median[1],median[2],median[3],
           min[0],max[0],min[1],max[1],min[2],max[2],min[3],max[3],(uint64_t)SINK);
    dlclose(handle);
    return 0;
}
