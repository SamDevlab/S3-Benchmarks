/* Independent native C timing harness + mathematical oracle.
 * ALL timed stencil computation is performed by S3-produced ELF libraries.
 * C does not replace the S3 kernel inside timed loops.
 */
#define _POSIX_C_SOURCE 200809L
#include <stdint.h>
#include <inttypes.h>
#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <dlfcn.h>

typedef int64_t (*stencil_fn)(const int64_t*,int64_t,int64_t);
static volatile uint64_t sink;

static double now_ns(void) {
    struct timespec t;
    if(clock_gettime(CLOCK_MONOTONIC_RAW,&t))exit(2);
    return (double)t.tv_sec*1e9+(double)t.tv_nsec;
}
static int cmp(const void *a,const void *b) {
    const double x=*(const double*)a,y=*(const double*)b;
    return (x>y)-(x<y);
}
static int64_t reference(const int64_t *grid,int w,int h) {
    int64_t total=0;
    for(int y=1;y<h-1;y++){
        for(int x=1;x<w-1;x++){
            int p=y*w+x;
            total+=grid[p-w-1]+grid[p-w]+grid[p-w+1]+grid[p-1]+grid[p+1]
                 +grid[p+w-1]+grid[p+w]+grid[p+w+1];
        }
    }
    return total;
}
int main(int argc,char**argv) {
    if(argc!=4){
        fprintf(stderr,"usage: stencil_native_ab_v16 BASE.so V16.so ROUNDS\n");
        return 2;
    }
    int rounds=atoi(argv[3]);
    if(rounds<5||rounds>31)return 3;
    void *libs[2];
    for(int i=0;i<2;i++){
        libs[i]=dlopen(argv[i+1],RTLD_NOW|RTLD_LOCAL);
        if(!libs[i]){
            fprintf(stderr,"dlopen:%s\n",dlerror());return 4;
        }
    }
    const int widths[]={8,16,24};
    const int heights[]={64,256,1024};
    int comma=0;
    printf("{\"cases\":[");
    for(int wi=0;wi<3;wi++){
        int w=widths[wi];
        char name[64];
        snprintf(name,sizeof(name),"stencil8_w%d",w);
        stencil_fn fn[2]={0};
        for(int k=0;k<2;k++){
            *(void**)(&fn[k])=dlsym(libs[k],name);
            if(!fn[k])return 5;
        }
        for(int hi=0;hi<3;hi++){
            int h=heights[hi];
            int64_t len=(int64_t)w*h;
            int64_t *grid=calloc((size_t)len,sizeof(int64_t));
            if(!grid)return 6;
            for(int64_t i=0;i<len;i++)grid[i]=(i*17+11)%11;
            int64_t expected=reference(grid,w,h);
            for(int k=0;k<2;k++){
                for(int j=0;j<3;j++){
                    int hh=j==0?3:j==1?h/2:h;
                    int64_t got=fn[k](grid,len,hh);
                    int64_t want=reference(grid,w,hh);
                    if(got!=want){
                        fprintf(stderr,"PARITY_FAIL w=%d h=%d checked=%d variant=%d got=%"PRId64" wanted=%"PRId64"\n",
                                w,h,hh,k,got,want);
                        return 7;
                    }
                }
            }
            int repetitions=h==64?50:h==256?15:4;
            double times[2][31]={{0}};
            for(int round=0;round<rounds;round++){
                for(int r=0;r<2;r++){
                    int which=(round+r)&1;
                    stencil_fn call=fn[which];
                    sink^=(uint64_t)call(grid,len,h);
                    double start=now_ns();
                    uint64_t result=0;
                    for(int j=0;j<repetitions;j++){
                        result+=(uint64_t)call(grid,len,h);
                    }
                    double elapsed=(now_ns()-start)/repetitions;
                    times[which][round]=elapsed;
                    sink^=result;
                }
            }
            for(int k=0;k<2;k++){
                qsort(times[k],(size_t)rounds,sizeof(double),cmp);
            }
            double baseline=times[0][rounds/2];
            double optimized=times[1][rounds/2];
            printf("%s{\"width\":%d,\"height\":%d,\"neighbors\":8,\"exact_reference\":%"PRId64",\"parity\":true,\"baseline_ns\":%.3f,\"v16_ns\":%.3f,\"speedup\":%.6f}",
                    comma++?",":"",w,h,expected,
                    baseline,optimized,baseline/optimized);
            free(grid);
        }
    }
    printf("],\"rounds\":%d,\"sink\":%"PRIu64"}\n",rounds,(uint64_t)sink);
    for(int i=0;i<2;i++)dlclose(libs[i]);
    return 0;
}
