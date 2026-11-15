"""V13 A/B: source-level inlining of rotation helper vs normal CTZ."""
from __future__ import annotations
import json
from pathlib import Path
import subprocess
import tempfile

from native_ctz_v13 import source_for,assembly_stats,S3_ROOT,HERE
from bootstrap.s3.pipeline import compile_source,OptimizationLevel
from bootstrap.s3.gf2_ir_certificate import certify_gf2_ir
from bootstrap.s3.gf2_dynamic_native import compile_certified_gf2_dynamic

def run():
    report={"campaign":"S3_V13_INLINE_ROTATION_AB",
            "status":"EXPERIMENTAL_NO_AUTO_PROMOTION",
            "cases":[],"rounds":9}
    with tempfile.TemporaryDirectory(prefix="s3_v13_inline_") as td:
        executable=Path(td)/"bench_inline"
        subprocess.run([
            "gcc","-O3","-std=c11","-Wall","-Wextra","-Werror",
            str(HERE.parent/"v12_core"/"compare_s3_native_v12.c"),
            "-o",str(executable),"-ldl",
        ],check=True,capture_output=True,timeout=60)
        for width,taps in ((8,(1,7)),(23,(1,11,12,16,21)),
                           (31,(0,1,3)),(32,(0,1,3))):
            ir,_=compile_source(
                source_for(width,taps),optimization=OptimizationLevel.O1,
                predictive_exact=False,
            ).require_ordinary_artifacts()
            cert=certify_gf2_ir(ir,"update",width)
            with (
                compile_certified_gf2_dynamic(
                    ir,cert,algorithm="generic",enable_experimental=True) as generic,
                compile_certified_gf2_dynamic(
                    ir,cert,algorithm="auto",enable_experimental=True,
                    codegen_variant="v13_ctz") as ctz,
                compile_certified_gf2_dynamic(
                    ir,cert,algorithm="auto",enable_experimental=True,
                    codegen_variant="v13_ctz_inline") as inline,
            ):
                libs=[Path(x._temp.name)/"dynamic.so" for x in (generic,ctz,inline)]
                case={"width":width,"taps":taps,"samples":[],
                      "assembly":{
                          k:assembly_stats(f)
                          for k,f in zip(("v13_ctz","v13_inline"),libs[1:])
                      }}
                for n in (1,64,1000003):
                    sample=json.loads(subprocess.check_output(
                        [str(executable),*(str(f) for f in libs),
                         str(width),str(cert.columns[0]),str(n),"9","1467813"],
                        text=True,timeout=90,
                    ))
                    assert sample["parity"]
                    base=sample["median_ns"]["s3_v11"]
                    candidate=sample["median_ns"]["s3_v12"]
                    case["samples"].append({"N":n,"ctz_ns":base,
                                            "inline_ns":candidate,
                                            "gain":base/candidate,
                                            "parity":True})
                    print(f"INLINE_W{width}_N{n} ctz={base:.1f}ns "
                          f"inline={candidate:.1f}ns ratio={base/candidate:.2f}",flush=True)
                report["cases"].append(case)
    target=HERE/"results_inline_ab_v13.json"
    target.write_text(json.dumps(report,indent=2),encoding="utf-8")
    print("RESULT_FILE="+str(target),flush=True)

if __name__=="__main__":
    run()
