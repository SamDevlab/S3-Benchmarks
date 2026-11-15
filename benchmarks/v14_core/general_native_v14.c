/* V14 independent A/B harness for S3 native x86 non-GF2 integer kernels.
 * The C reference does not compile any S3 code. Compiler baseline and
 * experimental backends yield separate S3-generated ELF shared libraries. */
#define _POSIX_C_SOURCE 200809L
#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
#include <inttypes.h>
#include <time.h>
#include <dlfcn.h>

typedef int64_t (*fn1)(int64_t);
struct runtime {
    void *lib;
    fn1 squares,factorial,popcount;
};
static volatile uint64_t sink;

static uint64_t reference(int kind,int64_t n) {
    if(kind==0){uint64_t sum=0;for(int64_t i=0;i<n;i++)sum+=(uint64_t)(i*i);return sum;}
    if(kind==1){uint64_t x=1;for(int64_t i=1;i<=n;i++)x*=i;return x;}
    return (uint64_t)__builtin_popcountll((uint64_t)n);
}
static double ns_now(void) {
    struct timespec t;
    if(clock_gettime(CLOCK_MONOTONIC_RAW,&t))exit(2);
    return (double)t.tv_sec*1e9+(double)t.tv_nsec;
}
static int cmp_double(const void *l,const void *r){
    const double a=*(const double*)l,b=*(const double*)r;
    return (a>b)-(a<b);
}
int main(int argc,char **argv) {
    if(argc!=4){fprintf(stderr,"usage: bench baseline.so optimized.so rounds\n");return 2;}
    int rounds=atoi(argv[3]);
    if(rounds<3||rounds>31)return 3;
    struct runtime r[2]={0};
    for(int i=0;i<2;i++){
        r[i].lib=dlopen(argv[i+1],RTLD_NOW|RTLD_LOCAL);
        if(!r[i].lib){fprintf(stderr,"dlopen: %s\n",dlerror());return 4;}
        *(void**)(&r[i].squares)=dlsym(r[i].lib,"sum_squares");
        *(void**)(&r[i].factorial)=dlsym(r[i].lib,"factorial");
        *(void**)(&r[i].popcount)=dlsym(r[i].lib,"count_bits");
        if(!r[i].squares||!r[i].factorial||!r[i].popcount)return 5;
    }
    const struct {const char*name;int kind;int64_t arg;int reps;} cases[]={
        {"sum_squares_32",0,32,500},
        {"sum_squares_512",0,512,200},
        {"sum_squares_4096",0,4096,50},
        {"factorial_12",1,12,1500},
        {"count_bits_2p31",2,INT64_C(2147483647),1500}
    };
    const int count=(int)(sizeof(cases)/sizeof(cases[0]));
    printf("{\"cases\":[");
    for(int i=0;i<count;i++){
        fn1 methods[2]={
            cases[i].kind==0?r[0].squares:cases[i].kind==1?r[0].factorial:r[0].popcount,
            cases[i].kind==0?r[1].squares:cases[i].kind==1?r[1].factorial:r[1].popcount
        };
        uint64_t expected=reference(cases[i].kind,cases[i].arg);
        for(int x=0;x<2;x++){
            for(int64_t k=0;k<15;k++){
                int64_t n=cases[i].arg;
                if(cases[i].kind==0)n=k*31;
                if(cases[i].kind==1)n=k%13;
                if(cases[i].kind==2)n=((uint64_t)cases[i].arg>>k)&INT64_MAX;
                if((uint64_t)methods[x](n)!=reference(cases[i].kind,n)){
                    fprintf(stderr,"PARITY_FAIL case=%s kind=%d n=%"PRId64"\n",cases[i].name,x,n);return 7;
                }
            }
            if((uint64_t)methods[x](cases[i].arg)!=expected)return 8;
        }
        double samples[2][31]={{0}};
        for(int round=0;round<rounds;round++){
            for(int j=0;j<2;j++){
                int variant=(round+j)&1;
                uint64_t z=0;
                fn1 f=methods[variant];
                z+=(uint64_t)f(cases[i].arg);
                double t=ns_now();
                for(int k=0;k<cases[i].reps;k++){
                    z+=(uint64_t)f(cases[i].arg);
                }
                samples[variant][round]=(ns_now()-t)/cases[i].reps;
                sink^=z;
            }
        }
        for(int v=0;v<2;v++)qsort(samples[v],(size_t)rounds,sizeof(double),cmp_double);
        double a=samples[0][rounds/2],b=samples[1][rounds/2];
        printf("%s{\"name\":\"%s\",\"input\":%"PRId64",\"parity\":true,\"baseline_ns\":%.4f,\"experimental_ns\":%.4f,\"speedup\":%.6f}",
            i?",":"",cases[i].name,cases[i].arg,a,b,a/b);
    }
    printf("],\"rounds\":%d,\"checksum\":%"PRIu64"}\n",rounds,(uint64_t)sink);
    for(int i=0;i<2;i++)dlclose(r[i].lib);
    return 0;
}
