#define _GNU_SOURCE
#include <dlfcn.h>
#include <stdio.h>
#include <stdlib.h>
typedef double (*fn_t)(double);
int main(int argc, char **argv) {
    if (argc != 4) return 2;
    void *h = dlopen(argv[1], RTLD_NOW | RTLD_LOCAL); if (!h) return 3;
    fn_t fn = (fn_t)dlsym(h, argv[2]); if (!fn) return 4;
    int calls = atoi(argv[3]);
    for (int i = 0; i < calls; ++i) { printf("CALL=%d\n", i); fflush(stdout); (void)fn(1.25); }
    puts("DONE"); fflush(stdout); dlclose(h); return 0;
}
