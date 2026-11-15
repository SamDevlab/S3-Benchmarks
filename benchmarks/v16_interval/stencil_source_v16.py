"""Deterministic S3 2D Conway-neighborhood stencil sum (i64 exact)."""
from __future__ import annotations
from hashlib import sha256

WIDTHS=(8,16,24)


def offsets(width:int)->tuple[int,...]:
    assert width>=3 and 2*width+2<=64
    return (0,1,2,width,width+2,2*width,2*width+1,2*width+2)


def kernel_name(width:int)->str:
    return f"stencil8_w{width}"


def source_for(width:int)->str:
    o=offsets(width)
    declare="\n".join(
        f"            mut index_{i}: i64 = base + {i}"
        for i in o[1:]
    )
    # The first two slice reads are the interval endpoints.
    loads=["xs[base]",f"xs[index_{o[-1]}]"]
    loads += [f"xs[index_{i}]" for i in o[1:-1]]
    expr=" + ".join(loads)
    return f"""export fn {kernel_name(width)}(xs: &[i64], height: i64) -> i64:
    mut max_y: i64 = height - 1
    mut max_x: i64 = {width-1}
    mut y: i64 = 1
    mut total: i64 = 0
    while y < max_y:
        mut x: i64 = 1
        while x < max_x:
            mut previous_y: i64 = y - 1
            mut row_base: i64 = previous_y * {width}
            mut previous_x: i64 = x - 1
            mut base: i64 = row_base + previous_x
{declare}
            total = total + {expr}
            x = x + 1
        y = y + 1
    return total
"""


def whole_source()->str:
    return "\n".join(source_for(w) for w in WIDTHS)+"\nfn main() -> i64:\n    return 0\n"


def sha256_hex()->str:
    return sha256(whole_source().encode()).hexdigest()
