#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
    long iterations = 50000;
    if (argc == 3 && argv[1][0] == '-' && argv[1][1] == 'i') {
        iterations = atol(argv[2]);
    }
    if (iterations < 1) iterations = 1;
    uint64_t value = 0x9e3779b97f4a7c15ULL;
    for (long i = 0; i < iterations; ++i) {
        value ^= value << 7;
        value ^= value >> 9;
        value += (uint64_t)i * 0x100000001b3ULL;
    }
    printf("%llu\n", (unsigned long long)value);
    return 0;
}
