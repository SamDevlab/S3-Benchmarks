"""Small paired native kernels used to promote P7, P8, and P9."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class NativeWorkload:
    workload_id: str
    name: str
    s3_source: str
    c_source: str
    operations_per_run: int
    supported_scope: str


P7_S3 = """\
fn p7_step(a: i64, b: i64) -> i64:
    mut product: i64 = a * b
    match product <=> 120:
        -1:
            product = product + 3
        0:
            product = product - 2
        1:
            product = product - 1
    return product

fn main() -> i64:
    mut outer: i64 = 0
    mut checksum: i64 = 0
    while outer <=> 64:
        mut inner: i64 = 0
        while inner <=> 64:
            checksum = checksum + p7_step(outer + 1, inner + 1)
            match checksum <=> 180:
                -1:
                    checksum = checksum
                0:
                    checksum = checksum - 180
                1:
                    checksum = checksum - 180
            inner = inner + 1
        outer = outer + 1
    return checksum
"""

P7_C = """\
#include <stdio.h>
static int p7_step(int a, int b) {
    int product = a * b;
    if (product < 120) product += 3;
    else if (product == 120) product -= 2;
    else product -= 1;
    return product;
}
int main(void) {
    int checksum = 0;
    for (int outer = 0; outer < 64; ++outer) {
        for (int inner = 0; inner < 64; ++inner) {
            checksum += p7_step(outer + 1, inner + 1);
            if (checksum >= 180) checksum -= 180;
        }
    }
    printf("program returned: %d\\n", checksum);
    return 0;
}
"""

P8_S3 = """\
fn p8_leaf(a: i64, b: i64, c: i64) -> i64:
    return a + b + c

fn p8_middle(a: i64, b: i64, c: i64) -> i64:
    return p8_leaf(a, b, c) + p8_leaf(c, a, b)

fn p8_outer(a: i64, b: i64) -> i64:
    return p8_middle(a, b, 3) + p8_middle(b, a, 4)

fn main() -> i64:
    mut index: i64 = 0
    mut checksum: i64 = 0
    while index <=> 64:
        checksum = checksum + p8_outer(index, index + 1)
        match checksum <=> 180:
            -1:
                checksum = checksum
            0:
                checksum = checksum - 180
            1:
                checksum = checksum - 180
        index = index + 1
    return checksum
"""

P8_C = """\
#include <stdio.h>
static int p8_leaf(int a, int b, int c) { return a + b + c; }
static int p8_middle(int a, int b, int c) {
    return p8_leaf(a, b, c) + p8_leaf(c, a, b);
}
static int p8_outer(int a, int b) {
    return p8_middle(a, b, 3) + p8_middle(b, a, 4);
}
int main(void) {
    int checksum = 0;
    for (int index = 0; index < 64; ++index) {
        checksum += p8_outer(index, index + 1);
        if (checksum >= 180) checksum -= 180;
    }
    printf("program returned: %d\\n", checksum);
    return 0;
}
"""

P9_S3 = """\
fn main() -> tryte:
    mut values: tryte[16] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    mut round: tryte = 0
    mut checksum: tryte = 0
    while round <=> 64:
        mut index: tryte = 0
        while index <=> 16:
            values[index] = values[index] + 1
            checksum = checksum + values[index]
            match checksum <=> 180:
                -1:
                    checksum = checksum
                0:
                    checksum = checksum - 180
                1:
                    checksum = checksum - 180
            index = index + 1
        round = round + 1
    return checksum
"""

P9_C = """\
#include <stdio.h>
int main(void) {
    int values[16] = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16};
    int checksum = 0;
    for (int round = 0; round < 64; ++round) {
        for (int index = 0; index < 16; ++index) {
            values[index] += 1;
            checksum += values[index];
            if (checksum >= 180) checksum -= 180;
        }
    }
    printf("program returned: %d\\n", checksum);
    return 0;
}
"""


NATIVE_WORKLOADS: tuple[NativeWorkload, ...] = (
    NativeWorkload("P7", "native arithmetic control", P7_S3, P7_C, 64 * 64, "S3_VS_C"),
    NativeWorkload("P8", "call stack and ABI", P8_S3, P8_C, 64 * 8, "S3_VS_C"),
    NativeWorkload("P9", "arrays and memory", P9_S3, P9_C, 64 * 16, "S3_VS_C"),
)
