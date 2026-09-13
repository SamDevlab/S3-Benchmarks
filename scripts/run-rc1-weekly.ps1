$ErrorActionPreference = "Stop"
python -m benchmarks.rc1.automation --mode weekly @args
exit $LASTEXITCODE
