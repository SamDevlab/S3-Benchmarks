/* Independent native Windows C reference for S3 Conway GPU semantics.
   Edges are zero, 32-bit binary cells, 8 neighbors, ping-pong.
   Host allocations/copies included in each call, not C compile time. */
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#if defined(_WIN32)
#define EXPORT __declspec(dllexport)
#else
#define EXPORT __attribute__((visibility("default")))
#endif

EXPORT int conway_native(const int32_t *initial, int32_t *output,
                         int32_t width, int32_t height, int32_t generations) {
    if (!initial || !output || width < 3 || height < 3 ||
        width > 32768 || height > 32768 || generations < 0 ||
        (int64_t)width * height > 262144) return -1;
    size_t count = (size_t)width * (size_t)height;
    size_t bytes = count * sizeof(int32_t);
    int32_t *a = (int32_t *)malloc(bytes);
    int32_t *b = (int32_t *)malloc(bytes);
    if (!a || !b) {
        free(a); free(b); return -2;
    }
    memcpy(a, initial, bytes);
    for (int32_t step=0; step<generations; step++) {
        memset(b, 0, bytes);
        for (int32_t y=1; y<height-1; y++) {
            int32_t row = y*width;
            for (int32_t x=1; x<width-1; x++) {
                int32_t p=row+x;
                int32_t neighbors = a[p-width-1] + a[p-width] + a[p-width+1] +
                                    a[p-1] + a[p+1] +
                                    a[p+width-1] + a[p+width] + a[p+width+1];
                b[p] = (neighbors==3 || (neighbors==2 && a[p]!=0)) ? 1 : 0;
            }
        }
        int32_t *swap = a; a=b; b=swap;
    }
    memcpy(output,a,bytes);
    free(a); free(b);
    return 0;
}
