$ErrorActionPreference = "Stop"
python -m benchmarks.rc1.automation --mode fast @args
exit $LASTEXITCODE
