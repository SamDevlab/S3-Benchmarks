/* V11: same-host real S3 x86-64 generic vs certificate-selected
 * cyclic polynomial algorithm; independent GCC specialist baseline.
 * C only supplies the benchmark harness/reference: both optimized
 * contenders are S3-compiler-produced ELF shared objects.
 */
#define _POSIX_C_SOURCE 200809L
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <dlfcn.h>
#include <inttypes.h>

typedef int64_t (*kernel_t)(int64_t,int64_t);
static kernel_t GENERIC, AUTOMATIC;
static int W;
static uint64_t MASK;
static volatile uint64_t SINK=0;

static uint64_t rotate_w(uint64_t x,int k) {
    k %= W;
    return k ? ((x << k) | (x >> (W-k))) & MASK : x & MASK;
}

static uint64_t poly_mul(uint64_t a,uint64_t b) {
    uint64_t result=0;
    while(a) {
        int i=__builtin_ctzll(a);
        result ^= rotate_w(b,i);
        a &= a-1;
    }
    return result&MASK;
}

__attribute__((noinline))
static uint64_t cyclic_reference(uint64_t x,uint64_t n) {
    uint64_t p=(UINT64_C(1)<<1) ^ (UINT64_C(1)<<(W-1));
    uint64_t acc=1;
    while(n) {
        if(n&1) acc=poly_mul(acc,p);
        n >>= 1;
        if(n) p=poly_mul(p,p);
    }
    return poly_mul(acc,x);
}

static uint64_t direct_n_steps(uint64_t x,uint64_t n) {
    while(n--) x=rotate_w(x,1) ^ rotate_w(x,W-1);
    return x&MASK;
}

static uint64_t execute(int mode,uint64_t x,uint64_t n) {
    if(mode==0) return (uint64_t)GENERIC((int64_t)x,(int64_t)n);
    if(mode==1) return (uint64_t)AUTOMATIC((int64_t)x,(int64_t)n);
    return cyclic_reference(x,n);
}

static double clock_ns(void) {
    struct timespec t;
    if(clock_gettime(CLOCK_MONOTONIC_RAW,&t)!=0) exit(9);
    return (double)t.tv_sec*1e9+(double)t.tv_nsec;
}

static int cmp(const void *a,const void*b) {
    double x=*(const double*)a,y=*(const double*)b;
    return (x>y)-(x<y);
}

int main(int argc,char **argv) {
    if(argc!=7) {
        fprintf(stderr,"usage: bench generic.so auto.so width N rounds seed\n");
        return 2;
    }
    W=atoi(argv[3]);
    uint64_t n=strtoull(argv[4],NULL,10);
    int rounds=atoi(argv[5]);
    uint64_t seed=strtoull(argv[6],NULL,10);
    if(W<2 || W>32 || n>(uint64_t)INT64_MAX || rounds<3 || rounds>31) return 3;
    MASK=(UINT64_C(1)<<W)-1;
    void *g=dlopen(argv[1],RTLD_NOW|RTLD_LOCAL);
    void *a=dlopen(argv[2],RTLD_NOW|RTLD_LOCAL);
    if(!g || !a) { fprintf(stderr,"dlopen: %s\n",dlerror()); return 4; }
    *(void**)(&GENERIC)=dlsym(g,"certified_step_dynamic");
    *(void**)(&AUTOMATIC)=dlsym(a,"certified_step_dynamic");
    if(!GENERIC || !AUTOMATIC) return 5;
    for(int k=0;k<64;++k) {
        uint64_t x=(seed+(uint64_t)k*UINT64_C(11400714819323198485))&MASK;
        uint64_t reference=direct_n_steps(x,n);
        if(reference!=execute(0,x,n) || reference!=execute(1,x,n)
                || reference!=execute(2,x,n)) {
            fprintf(stderr,"PARITY_FAIL W=%d N=%" PRIu64 " x=%" PRIu64 "\n",W,n,x);
            return 6;
        }
    }
    double samples[3][31],medians[3];
    const int batches[3]={300,700,10000};
    for(int round=0;round<rounds;++round) {
        for(int slot=0;slot<3;++slot) {
            int mode=(round+slot)%3;
            uint64_t sum=0;
            for(int warm=0;warm<8;++warm)
                sum ^= execute(mode,(seed+(uint64_t)(warm+round+1)*31)&MASK,n);
            double t0=clock_ns();
            for(int i=0;i<batches[mode];++i)
                sum ^= execute(mode,(seed+(uint64_t)(i+round+1)*1099511628211ULL)&MASK,n);
            double t1=clock_ns();
            SINK ^= sum;
            samples[mode][round]=(t1-t0)/batches[mode];
        }
    }
    for(int k=0;k<3;++k) {
        qsort(samples[k],rounds,sizeof(double),cmp);
        medians[k]=samples[k][rounds/2];
    }
    printf("{\"W\":%d,\"N\":%" PRIu64 ",\"rounds\":%d,\"differential_checks\":64,"
           "\"parity\":true,\"median_ns\":{\"s3_generic\":%.4f,"
           "\"s3_auto_selected\":%.4f,\"gcc_cyclic_specialist\":%.4f},"
           "\"auto_over_generic\":%.6f,\"auto_over_gcc_specialist\":%.6f,"
           "\"sink\":%" PRIu64 "}\n",
           W,n,rounds,medians[0],medians[1],medians[2],
           medians[1]/medians[0],medians[1]/medians[2],(uint64_t)SINK);
    dlclose(a);
    dlclose(g);
    return 0;
}
