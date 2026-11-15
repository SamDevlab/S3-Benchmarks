/* V15 native S3 x86 slice bounds reuse A/B. No C implementation is used
   to execute the S3 kernels. C provides an independent exact oracle and
   a low-overhead clocked caller to two S3 compiler-produced ELF libraries. */
#define _POSIX_C_SOURCE 200809L
#include <stdint.h>
#include <inttypes.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <time.h>
#include <dlfcn.h>

typedef int64_t (*kernel)(const int64_t*,int64_t,int64_t);
struct engine {void *lib;kernel loop_dup,sum_three;};
static volatile uint64_t sink;

static double now_ns(void){
    struct timespec t;
    if(clock_gettime(CLOCK_MONOTONIC_RAW,&t)!=0)exit(2);
    return (double)t.tv_sec*1e9+(double)t.tv_nsec;
}
static int cmpd(const void *a,const void *b){
    double x=*(const double*)a,y=*(const double*)b;
    return (x>y)-(x<y);
}
static int64_t expected(const int64_t *values,int64_t n,int repeat){
    int64_t sum=0;
    for(int64_t i=0;i<n;i++)sum+=values[i];
    return sum*repeat;
}
static void parity_or_exit(kernel fn,const int64_t *data,int64_t n,int repeat){
    const int64_t cases[]={0,1,2,13,n/2,n};
    for(size_t i=0;i<sizeof(cases)/sizeof(cases[0]);i++){
        int64_t count=cases[i];
        if(count>n)continue;
        const int64_t got=fn(data,n,count);
        if(got!=expected(data,count,repeat)){
            fprintf(stderr,"S3_NATIVE_PARITY_FAILURE n=%"PRId64" count=%"PRId64" got=%"PRId64" expected=%"PRId64"\n",
                    n,count,got,expected(data,count,repeat));
            exit(9);
        }
    }
}
int main(int argc,char **argv){
    if(argc!=5){
        fprintf(stderr,"usage: native_bounds_ab_v15 base.so experimental.so rounds mode\n");
        return 2;
    }
    const int rounds=atoi(argv[3]),mode=atoi(argv[4]);
    if(rounds<5||rounds>31||mode<0||mode>1)return 3;
    struct engine engines[2]={0};
    for(int i=0;i<2;i++){
        engines[i].lib=dlopen(argv[i+1],RTLD_NOW|RTLD_LOCAL);
        if(!engines[i].lib){
            fprintf(stderr,"dlopen failed: %s\n",dlerror());return 4;
        }
        *(void**)(&engines[i].loop_dup)=dlsym(engines[i].lib,"loop_dup");
        *(void**)(&engines[i].sum_three)=dlsym(engines[i].lib,"sum_three");
        if(!engines[i].loop_dup||!engines[i].sum_three)return 5;
    }
    const int64_t lengths[]={64,1024,8192};
    const char *names[]={"loop_dup","sum_three"};
    printf("{\"cases\":[");
    int comma=0;
    for(int kind=0;kind<2;kind++){
        for(int size=0;size<3;size++){
            int64_t n=lengths[size];
            int repeats=n==64?600:n==1024?150:30;
            int64_t *data=(int64_t*)calloc((size_t)n,sizeof(int64_t));
            if(!data)return 6;
            for(int64_t i=0;i<n;i++)data[i]=(i*17+11)%97;
            kernel methods[2]={
                kind==0?engines[0].loop_dup:engines[0].sum_three,
                kind==0?engines[1].loop_dup:engines[1].sum_three,
            };
            for(int i=0;i<2;i++)parity_or_exit(methods[i],data,n,kind==0?2:3);
            double samples[2][31]={{0}};
            for(int round=0;round<rounds;round++){
                for(int j=0;j<2;j++){
                    int variant=(round+j)&1;
                    kernel fn=methods[variant];
                    sink^=(uint64_t)fn(data,n,n);
                    double t=now_ns();
                    uint64_t checksum=0;
                    for(int k=0;k<repeats;k++){
                        checksum+=(uint64_t)fn(data,n,n);
                    }
                    samples[variant][round]=(now_ns()-t)/(double)repeats;
                    sink^=checksum;
                }
            }
            for(int variant=0;variant<2;variant++){
                qsort(samples[variant],(size_t)rounds,sizeof(double),cmpd);
            }
            double baseline=samples[0][rounds/2];
            double optimized=samples[1][rounds/2];
            printf("%s{\"kernel\":\"%s\",\"length\":%"PRId64",\"expected\":%"PRId64",\"parity\":true,\"baseline_ns\":%.3f,\"v15_ns\":%.3f,\"speedup\":%.6f}",
                  comma++?",":"",names[kind],n,
                  expected(data,n,kind==0?2:3),
                  baseline,optimized,baseline/optimized);
            free(data);
        }
    }
    printf("],\"rounds\":%d,\"mode\":%d,\"checksum\":%"PRIu64"}\n",rounds,mode,(uint64_t)sink);
    for(int i=0;i<2;i++)dlclose(engines[i].lib);
    return 0;
}
