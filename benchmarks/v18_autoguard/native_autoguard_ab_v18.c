/* Independent reference + native S3 ELF timing for dynamic-width stencils.
 * The C program computes oracle values OUTSIDE timed sections.
 * All timed stencil computations are in S3-produced x86-64 libraries.
 */
#define _POSIX_C_SOURCE 200809L
#include <stdint.h>
#include <inttypes.h>
#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <dlfcn.h>

typedef int64_t (*s3_stencil)(const int64_t*,int64_t,int64_t,int64_t);
static volatile uint64_t sink;

static double now_ns(void) {
    struct timespec ts;
    if (clock_gettime(CLOCK_MONOTONIC_RAW,&ts))exit(2);
    return (double)ts.tv_sec*1e9+(double)ts.tv_nsec;
}
static int compare(const void* a,const void* b) {
    double x=*(const double*)a,y=*(const double*)b;
    return (x>y)-(x<y);
}
static int64_t oracle(const int64_t* xs,int64_t width,int64_t height) {
    if(width<3)return 0;
    int64_t out=0;
    for(int64_t y=1;y<height-1;y++)
        for(int64_t x=1;x<width-1;x++) {
            int64_t base=(y-1)*width+(x-1);
            int64_t twice=width+width;
            out+=xs[base]+xs[base+twice+2]+xs[base+1]+xs[base+2]
                +xs[base+width]+xs[base+width+2]
                +xs[base+twice]+xs[base+twice+1];
        }
    return out;
}
int main(int argc,char**argv) {
    if(argc!=4){fprintf(stderr,"usage: native_dynamic_ab BASE.so V17.so ROUNDS\n");return 2;}
    const int rounds=atoi(argv[3]);
    if(rounds<5||rounds>31)return 3;
    void* dlls[2]={0};
    s3_stencil functions[2]={0};
    for(int v=0;v<2;v++){
        dlls[v]=dlopen(argv[v+1],RTLD_NOW|RTLD_LOCAL);
        if(!dlls[v]){fprintf(stderr,"dlopen:%s\n",dlerror());return 4;}
        *(void**)(&functions[v])=dlsym(dlls[v],"auto_stencil");
        if(!functions[v])return 5;
    }
    const int widths[]={3,5,8,16,31,48,64};
    const int heights[]={64,256,1024};
    int first=1;
    printf("{\"cases\":[");
    for(size_t wi=0;wi<sizeof(widths)/sizeof(widths[0]);wi++) {
        const int w=widths[wi];
        for(size_t hi=0;hi<sizeof(heights)/sizeof(heights[0]);hi++) {
            const int h=heights[hi];
            const int64_t n=(int64_t)w*h;
            int64_t* xs=calloc((size_t)n,sizeof(int64_t));
            if(!xs)return 6;
            for(int64_t i=0;i<n;i++)xs[i]=(i*17+11)%13;
            const int64_t expected=oracle(xs,w,h);
            for(int v=0;v<2;v++) {
                for(int k=0;k<4;k++){
                    int sample_h=k==0?3:k==1?4:k==2?h/2:h;
                    if (sample_h>h)continue;
                    int64_t got=functions[v](xs,n,w,sample_h);
                    if(got!=oracle(xs,w,sample_h)){
                        fprintf(stderr,"PARITY_FAILURE w=%d h=%d sample_h=%d var=%d got=%"PRId64" oracle=%"PRId64"\n",
                                w,h,sample_h,v,got,oracle(xs,w,sample_h));
                        return 7;
                    }
                }
            }
            int iterations=(n<=1000)?100:(n<=8000)?25:(n<=24000)?10:3;
            double measurements[2][31]={{0}};
            for(int round=0;round<rounds;round++) {
                for(int j=0;j<2;j++) {
                    int v=(round+j)&1;
                    s3_stencil fn=functions[v];
                    sink^=(uint64_t)fn(xs,n,w,h);
                    uint64_t check=0;
                    double start=now_ns();
                    for(int k=0;k<iterations;k++)check+=(uint64_t)fn(xs,n,w,h);
                    measurements[v][round]=(now_ns()-start)/iterations;
                    sink^=check;
                }
            }
            for(int v=0;v<2;v++)
                qsort(measurements[v],(size_t)rounds,sizeof(double),compare);
            const double baseline=measurements[0][rounds/2];
            const double optimized=measurements[1][rounds/2];
            printf("%s{\"width\":%d,\"height\":%d,\"expected\":%"PRId64",\"parity\":true,\"baseline_ns\":%.3f,\"v18_ns\":%.3f,\"speedup\":%.6f}",
                first?"":",",w,h,expected,baseline,optimized,baseline/optimized);
            first=0;
            free(xs);
        }
    }
    printf("],\"rounds\":%d,\"sink\":%"PRIu64"}\n",rounds,(uint64_t)sink);
    for(int v=0;v<2;v++)dlclose(dlls[v]);
    return 0;
}
