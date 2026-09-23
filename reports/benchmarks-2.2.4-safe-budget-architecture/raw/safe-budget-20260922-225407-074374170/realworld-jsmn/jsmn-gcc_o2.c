/* Auto-generated embedded C benchmark driver */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

#define JSMN_PARENT_LINKS
#include "jsmn.h"

#define MAX_TOKENS 32

static const char input_buffer[] = {123, 34, 97, 34, 58, 49, 44, 34, 98, 34, 58, 34, 118, 97, 108, 34, 44, 34, 99, 34, 58, 116, 114, 117, 101, 44, 34, 100, 34, 58, 110, 117, 108, 108, 125};
static const size_t input_len = 35;

int main(int argc, char **argv) {
    long iterations = 1250000;
    for (int i = 1; i < argc; i++) {
        if (strcmp(argv[i], "--loop") == 0 && i + 1 < argc) {
            iterations = atol(argv[i + 1]);
            break;
        }
    }
    if (iterations <= 0) iterations = 1;

    jsmn_parser parser;
    jsmntok_t tokens[MAX_TOKENS];

    int accum = 0;
    for (long i = 0; i < iterations; i++) {
        jsmn_init(&parser);
        int r = jsmn_parse(&parser, input_buffer, input_len, tokens, MAX_TOKENS);
        int val = (r >= 0) ? r : -r;
        accum += val;
        if (accum >= 200) {
            accum -= 200;
        }
    }

    printf("program returned: %d\n", accum);
    return 0;
}
