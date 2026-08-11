/*
 * c_runner.c - Standalone C driver for zserge/jsmn benchmark
 * 
 * Supports:
 *  - Correctness verification mode (--correctness)
 *  - Internal parse loop mode (--loop <N>) with observable modulo accumulator exit status
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

#define JSMN_PARENT_LINKS
#include "jsmn.h"

#define MAX_TOKENS 32
#define MAX_INPUT_LEN 4096

static int64_t compute_checksum(int status, jsmntok_t *tokens, int count) {
    if (status < 0) {
        return (int64_t)(status < 0 ? -status : status);
    }
    int64_t sum = status;
    for (int i = 0; i < count; i++) {
        sum += tokens[i].type;
        sum += tokens[i].start;
        sum += tokens[i].end;
        sum += tokens[i].size;
    }
    return sum;
}

int main(int argc, char **argv) {
    if (argc < 2) {
        fprintf(stderr, "Usage: %s [--correctness | --loop <iterations>] [json_string | --file <path>]\n", argv[0]);
        return 1;
    }

    int mode_correctness = 0;
    long iterations = 1;
    int arg_idx = 1;

    if (strcmp(argv[arg_idx], "--correctness") == 0) {
        mode_correctness = 1;
        arg_idx++;
    } else if (strcmp(argv[arg_idx], "--loop") == 0) {
        arg_idx++;
        if (arg_idx < argc) {
            iterations = atol(argv[arg_idx]);
            arg_idx++;
        }
        if (iterations <= 0) iterations = 1;
    }

    char buffer[MAX_INPUT_LEN + 1];
    memset(buffer, 0, sizeof(buffer));

    if (arg_idx < argc && strcmp(argv[arg_idx], "--file") == 0) {
        arg_idx++;
        if (arg_idx >= argc) {
            fprintf(stderr, "Error: --file requires a path\n");
            return 1;
        }
        FILE *f = fopen(argv[arg_idx], "rb");
        if (!f) {
            fprintf(stderr, "Error opening file: %s\n", argv[arg_idx]);
            return 1;
        }
        size_t n = fread(buffer, 1, MAX_INPUT_LEN, f);
        buffer[n] = '\0';
        fclose(f);
    } else if (arg_idx < argc) {
        strncpy(buffer, argv[arg_idx], MAX_INPUT_LEN);
        buffer[MAX_INPUT_LEN] = '\0';
    } else {
        size_t n = fread(buffer, 1, MAX_INPUT_LEN, stdin);
        buffer[n] = '\0';
    }

    size_t len = strlen(buffer);
    jsmn_parser parser;
    jsmntok_t tokens[MAX_TOKENS];

    if (mode_correctness) {
        jsmn_init(&parser);
        int r = jsmn_parse(&parser, buffer, len, tokens, MAX_TOKENS);
        int token_count = (r >= 0) ? r : 0;
        int64_t chk = compute_checksum(r, tokens, token_count);

        printf("{\"status\":%d,\"token_count\":%d,\"checksum\":%lld,\"tokens\":[", r, token_count, (long long)chk);
        for (int i = 0; i < token_count; i++) {
            printf("{\"type\":%d,\"start\":%d,\"end\":%d,\"size\":%d}%s",
                   tokens[i].type, tokens[i].start, tokens[i].end, tokens[i].size,
                   (i == token_count - 1) ? "" : ",");
        }
        printf("]}\n");
        return 0;
    }

    // Native internal parse loop with anti-DCE observable exit status
    int64_t accum = 0;
    for (long i = 0; i < iterations; i++) {
        jsmn_init(&parser);
        int r = jsmn_parse(&parser, buffer, len, tokens, MAX_TOKENS);
        int token_count = (r >= 0) ? r : 0;
        int64_t chk = compute_checksum(r, tokens, token_count);
        accum = (accum + chk) % 251;
    }

    // Return observable anti-DCE modulo checksum as process exit status
    return (int)(accum & 0xFF);
}
