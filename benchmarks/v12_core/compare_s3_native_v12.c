/* V12: independent C harness for generic S3, V11 S3, V12 S3,
 * GCC algorithm-matched scan reference, GCC sparse specialist.
 * Only GCC assembles/links the S3-produced x86 assembly.
 * One-device experiment; no claims about other machines.
 */
#define _POSIX_C_SOURCE 200809L
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <inttypes.h>
#include <dlfcn.h>

typedef int64_t (*kernel_t)(int64_t,int64_t);
static kernel_t GENERIC,V11,V12;
static uint64_t MASK,P;
static int W;
static volatile uint64_t SINK;

static uint64_t rot(uint64_t a,int k) {
    k %= W;
    return k ? ((a<<k)|(a>>(W-k)))&MASK : a&MASK;
}
static uint64_t mul_scan(uint64_t a,uint64_t b) {
    uint64_t out=0;
    for(int k=0;k<W;k++) out ^= rot(b,k)*((a>>k)&1);
    return out&MASK;
}
static uint64_t square_scan(uint64_t a) {
    uint64_t out=0;
    for(int k=0;k<W;k++) out ^= ((a>>k)&1) << ((2*k)%W);
    return out&MASK;
}
static uint64_t mul_sparse(uint64_t a,uint64_t b) {
    uint64_t out=0;
    while(a) {
        int bit=__builtin_ctzll(a);
        out ^= rot(b,bit);
        a&=a-1;
    }
    return out&MASK;
}
__attribute__((noinline,noclone))
static uint64_t c_scan(uint64_t state,uint64_t n) {
    uint64_t coeff=1,base=P;
    while(n) {
        uint64_t prod=mul_scan(coeff,base);
        uint64_t bit=n&1;
        coeff=coeff+(prod-coeff)*bit;
        n/=2;
        base=square_scan(base);
    }
    return mul_scan(coeff,state);
}
__attribute__((noinline,noclone))
static uint64_t c_sparse(uint64_t state,uint64_t n) {
    uint64_t coeff=1,base=P;
    while(n) {
        if(n&1) coeff=mul_sparse(coeff,base);
        n/=2;
        if(n) base=mul_sparse(base,base);
    }
    return mul_sparse(coeff,state);
}
static uint64_t direct_step(uint64_t x) {
    uint64_t result=0;
    for(int k=0;k<W;k++) if(P & (UINT64_C(1)<<k)) result ^= rot(x,k);
    return result&MASK;
}
static uint64_t direct(uint64_t x,uint64_t n) {
    while(n--) x=direct_step(x);
    return x;
}
static uint64_t call_mode(int mode,uint64_t x,uint64_t n) {
    if(mode==0) return (uint64_t)GENERIC((int64_t)x,(int64_t)n);
    if(mode==1) return (uint64_t)V11((int64_t)x,(int64_t)n);
    if(mode==2) return (uint64_t)V12((int64_t)x,(int64_t)n);
    if(mode==3) return c_scan(x,n);
    return c_sparse(x,n);
}
static double ns_now(void) {
    struct timespec t;
    if(clock_gettime(CLOCK_MONOTONIC_RAW,&t)!=0) exit(7);
    return (double)t.tv_sec*1e9+(double)t.tv_nsec;
}
static int compare(const void *aa,const void *bb) {
    double a=*(const double*)aa,b=*(const double*)bb;
    return (a>b)-(a<b);
}
int main(int argc,char **argv) {
    if(argc!=9) {
        fprintf(stderr,"usage: bench generic.so v11.so v12.so W P N rounds seed\n");
        return 2;
    }
    W=atoi(argv[4]); P=strtoull(argv[5],0,0);
    uint64_t n=strtoull(argv[6],0,10),seed=strtoull(argv[8],0,10);
    int rounds=atoi(argv[7]);
    if(W<2 || W>32 || P >= (UINT64_C(1)<<W) ||
       n>(uint64_t)INT64_MAX || rounds<3 || rounds>31) return 3;
    MASK=(UINT64_C(1)<<W)-1;
    void *libs[3];
    kernel_t *slots[3]={&GENERIC,&V11,&V12};
    for(int k=0;k<3;k++) {
        libs[k]=dlopen(argv[1+k],RTLD_NOW|RTLD_LOCAL);
        if(!libs[k]) {fprintf(stderr,"dlopen: %s\n",dlerror());return 4;}
        *(void**)slots[k]=dlsym(libs[k],"certified_step_dynamic");
        if(!*slots[k]) return 5;
    }
    for(int k=0;k<64;k++) {
        uint64_t x=(seed+(uint64_t)k*UINT64_C(11400714819323198485))&MASK;
        uint64_t ref=c_sparse(x,n);
        for(int mode=0;mode<4;mode++) {
            if(call_mode(mode,x,n)!=ref) {
                fprintf(stderr,"PARITY_FAIL W=%d P=%"PRIu64" N=%"PRIu64
                        " mode=%d x=%"PRIu64"\n",W,P,n,mode,x);
                return 6;
            }
        }
        if(n<=4096 || k<4) {
            if(direct(x,n)!=ref) {
                fprintf(stderr,"DIRECT_PARITY_FAIL W=%d N=%"PRIu64"\n",W,n);
                return 8;
            }
        }
    }
    double samples[5][31],median[5]={0};
    const int batches[5]={300,500,500,1500,4000};
    for(int round=0;round<rounds;round++) {
        for(int slot=0;slot<5;slot++) {
            int mode=(round+slot)%5;
            uint64_t sum=0;
            for(int i=0;i<8;i++)
                sum ^= call_mode(mode,(seed+(uint64_t)(i+round+1)*31)&MASK,n);
            double start=ns_now();
            for(int i=0;i<batches[mode];i++)
                sum ^= call_mode(mode,(seed+(uint64_t)(i+round+1)*1099511628211ULL)&MASK,n);
            double end=ns_now();
            SINK ^= sum;
            samples[mode][round]=(end-start)/batches[mode];
        }
    }
    for(int k=0;k<5;k++) {
        qsort(samples[k],rounds,sizeof(double),compare);
        median[k]=samples[k][rounds/2];
    }
    printf("{\"W\":%d,\"P\":%"PRIu64",\"N\":%"PRIu64
           ",\"rounds\":%d,\"parity\":true,\"checks\":64,\"median_ns\":"
           "{\"s3_generic\":%.3f,\"s3_v11\":%.3f,\"s3_v12\":%.3f,"
           "\"gcc_matched_scan\":%.3f,\"gcc_sparse\":%.3f},"
           "\"v12_over_v11\":%.6f,\"v12_over_gcc_matched\":%.6f,"
           "\"v12_over_gcc_sparse\":%.6f,\"sink\":%"PRIu64"}\n",
           W,P,n,rounds,median[0],median[1],median[2],median[3],median[4],
           median[2]/median[1],median[2]/median[3],median[2]/median[4],
           (uint64_t)SINK);
    for(int k=0;k<3;k++) dlclose(libs[k]);
    return 0;
}
