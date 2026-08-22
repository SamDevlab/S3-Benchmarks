$ErrorActionPreference = "Stop"
python -m benchmarks.rc1.automation --mode nightly @args
exit $LASTEXITCODE
