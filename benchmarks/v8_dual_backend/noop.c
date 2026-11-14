#include <stdint.h>
/* CALL_OVERHEAD_BASELINE: same call shape (dlsym + indirect call + i64 ABI) as the measured functions. */
int64_t noop1(int64_t a) { return a; }
int64_t noop2(int64_t a, int64_t b) { return a ^ b; }
int64_t noop3(int64_t a, int64_t b, int64_t c) { return a ^ b ^ c; }
