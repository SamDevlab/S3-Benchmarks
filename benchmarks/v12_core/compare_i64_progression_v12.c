/* V12 actual S3-native checked i64 arithmetic progression vs GCC C formula.
 * The baseline is the original S3 UPDATE called N times; fast native is
 * a *new S3-compiled* fixed formula taking dynamic N; GCC is independent.
 * The test domain stays within checked i64 bounds.
 */
#define _POSIX_C_SOURCE 200809L
#include <stdint.h>
#include <inttypes.h>
#include <stdio.h>
#include <stdlib.h>
#include <dlfcn.h>
#include <time.h>

typedef int64_t (*update_t)(int64_t);
typedef int64_t (*advance_t)(int64_t,int64_t);
static update_t S3_BASE;
static advance_t S3_FAST;
static volatile int64_t SINK;

static int64_t c_closed_form(int64_t x,int64_t n,int64_t delta) {
    __int128 v=(__int128)x+(__int128)n*delta;
    if(v<INT64_MIN || v>INT64_MAX) exit(7);
    return (int64_t)v;
}

static int64_t direct_s3(int64_t x,int64_t n) {
    while(n--) x=S3_BASE(x);
    return x;
}

static int64_t method(int mode,int64_t x,int64_t n,int64_t d) {
    if(mode==0) return direct_s3(x,n);
    if(mode==1) return S3_FAST(x,n);
    return c_closed_form(x,n,d);
}
static double now_ns(void) {
    struct timespec x;
    if(clock_gettime(CLOCK_MONOTONIC_RAW,&x)) exit(8);
    return (double)x.tv_sec*1e9+(double)x.tv_nsec;
}
static int cmp(const void*aa,const void*bb) {
    double a=*(const double*)aa,b=*(const double*)bb;
    return (a>b)-(a<b);
}

int main(int argc,char**argv) {
    if(argc!=7) {fprintf(stderr,"usage: original.so native.so delta N rounds seed\n");return 2;}
    void *o=dlopen(argv[1],RTLD_NOW|RTLD_LOCAL);
    void *f=dlopen(argv[2],RTLD_NOW|RTLD_LOCAL);
    if(!o || !f) {fprintf(stderr,"dlopen failed\n");return 3;}
    *(void**)(&S3_BASE)=dlsym(o,"update");
    *(void**)(&S3_FAST)=dlsym(f,"certified_step_dynamic");
    if(!S3_BASE || !S3_FAST) {fprintf(stderr,"symbol missing\n");return 4;}
    int64_t delta=strtoll(argv[3],NULL,10);
    int64_t n=strtoll(argv[4],NULL,10);
    int rounds=atoi(argv[5]);
    int64_t seed=strtoll(argv[6],NULL,10);
    if(n<0 || rounds<7 || rounds>31) return 5;
    for(int k=0;k<64;++k) {
        int64_t state=seed+(k-32)*113;
        int64_t reference=c_closed_form(state,n,delta);
        for(int mode=0;mode<3;++mode)
            if(method(mode,state,n,delta)!=reference) {
                fprintf(stderr,"PARITY_FAIL state=%" PRId64 " N=%" PRId64 "\n",state,n);
                return 6;
            }
    }
    double samples[3][31],med[3];
    int batches[3]={n>100000?2:(n>10000?10:100),900,12000};
    for(int r=0;r<rounds;++r) {
        for(int slot=0;slot<3;++slot) {
            int mode=(r+slot)%3;
            int64_t accumulator=0;
            for(int w=0;w<8;++w)
                accumulator ^= method(mode,seed+r+w,n,delta);
            double t0=now_ns();
            for(int j=0;j<batches[mode];++j)
                accumulator ^= method(mode,seed+r+j*3,n,delta);
            double t1=now_ns();
            SINK ^= accumulator;
            samples[mode][r]=(t1-t0)/batches[mode];
        }
    }
    for(int k=0;k<3;++k){
        qsort(samples[k],rounds,sizeof(double),cmp);
        med[k]=samples[k][rounds/2];
    }
    printf("{\"N\":%" PRId64 ",\"delta\":%" PRId64 ",\"rounds\":%d,"
           "\"differential_states\":64,\"parity\":true,"
           "\"median_ns\":{\"original_s3_n_steps\":%.5f,"
           "\"verified_native_s3_formula\":%.5f,\"independent_gcc_formula\":%.5f},"
           "\"native_speedup_over_original\":%.6f,\"sink\":%" PRId64 "}\n",
           n,delta,rounds,med[0],med[1],med[2],med[0]/med[1],(int64_t)SINK);
    dlclose(f);
    dlclose(o);
    return 0;
}
