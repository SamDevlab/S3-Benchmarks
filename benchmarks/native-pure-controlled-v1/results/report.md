# Native S3 Pure vs Controlled — measurement report

- Campaign: `S3_NATIVE_PURE_VS_CONTROLLED_CROSS_LANGUAGE_BENCHMARK_V1`
- Result: **COMPLETE**; `6` workloads, `4590` measured cells.
- V6 baseline: `2eab8a43f07b7fc842c4036ea0fb0203a9d41d6c`; experimental profile commit: `87c0a5be070210f158313a4d272fbdd795536232` (direct child).
- Host: AMD Ryzen 5 3400G with Radeon Vega Graphics, Linux-7.0.0-31-generic-x86_64-with-glibc2.43; CPU affinity 0; governor unavailable.
- Fixture SHA-256: `870150e16732b81a733af584cb68b1ddddfb47fa06ee7f8a9d6248a99b099a8d`; generated source bundle SHA-256: `9d5159268e0a6f1f388ff33ec1f611dffff73f3c5989c8cbdda22a9e21b84e86`.
- Sampling: 3 warmups + 15 rounds; input sizes small, medium, full; raw outliers retained.
- The native timer covers repeated indirect FFI calls only. Dispatch overhead is included, not subtracted. Python is timed separately as interpreted code.
- The full root filesystem forced all generated artifacts/caches into `/dev/shm`. These are KVM-guest descriptive measurements, not bare-metal claims.

## Kernel runtime

Times are nanoseconds per call; optimization levels are tool-specific and not asserted equivalent. p95 is the empirical nearest-rank estimate from 15 samples. CV is population standard deviation / mean.

| Workload | Input | Implementation | Median ns/call | p95 ns/call | CV | Median RSS KiB |
|---|---:|---|---:|---:|---:|---:|
| `agent_energy_residual` | small | S3 Pure O1 | 4096.25 | 6482.50 | 0.223 | 21688 |
| `agent_energy_residual` | small | S3 Per-instruction O1 | 4255.00 | 5362.50 | 0.249 | 21688 |
| `agent_energy_residual` | small | S3 Exact-segment O1 | 4437.50 | 10420.00 | 0.401 | 21688 |
| `agent_energy_residual` | small | S3 Loop-hybrid O1 | 4171.25 | 12525.00 | 0.470 | 21688 |
| `agent_energy_residual` | small | GCC O2 | 125.00 | 266.25 | 0.300 | 21688 |
| `agent_energy_residual` | small | Clang O2 | 117.50 | 170.00 | 0.203 | 21688 |
| `agent_energy_residual` | small | Rust opt-level 2 | 113.75 | 177.50 | 0.223 | 21688 |
| `agent_energy_residual` | small | Zig ReleaseFast | 105.00 | 227.50 | 0.323 | 21688 |
| `agent_energy_residual` | small | Python interpreted | 6923.62 | 11001.00 | 0.232 | 21688 |
| `agent_energy_residual` | medium | S3 Pure O1 | 15450.00 | 35020.00 | 0.386 | 21688 |
| `agent_energy_residual` | medium | S3 Per-instruction O1 | 15675.00 | 18720.00 | 0.242 | 21688 |
| `agent_energy_residual` | medium | S3 Exact-segment O1 | 13830.00 | 35300.00 | 0.412 | 21688 |
| `agent_energy_residual` | medium | S3 Loop-hybrid O1 | 13440.00 | 17080.00 | 0.224 | 21688 |
| `agent_energy_residual` | medium | GCC O2 | 530.00 | 815.00 | 0.154 | 21688 |
| `agent_energy_residual` | medium | Clang O2 | 465.00 | 635.00 | 0.174 | 21688 |
| `agent_energy_residual` | medium | Rust opt-level 2 | 415.00 | 800.00 | 0.276 | 21688 |
| `agent_energy_residual` | medium | Zig ReleaseFast | 380.00 | 445.00 | 0.121 | 21688 |
| `agent_energy_residual` | medium | Python interpreted | 25454.50 | 59769.00 | 0.411 | 21688 |
| `agent_energy_residual` | full | S3 Pure O1 | 39040.00 | 54990.00 | 0.221 | 21688 |
| `agent_energy_residual` | full | S3 Per-instruction O1 | 42550.00 | 136260.00 | 0.581 | 21688 |
| `agent_energy_residual` | full | S3 Exact-segment O1 | 42420.00 | 62760.00 | 0.247 | 21688 |
| `agent_energy_residual` | full | S3 Loop-hybrid O1 | 46330.00 | 146939.00 | 0.515 | 21688 |
| `agent_energy_residual` | full | GCC O2 | 1180.00 | 1610.00 | 0.139 | 21688 |
| `agent_energy_residual` | full | Clang O2 | 1130.00 | 1350.00 | 0.135 | 21688 |
| `agent_energy_residual` | full | Rust opt-level 2 | 1090.00 | 30690.00 | 2.446 | 21688 |
| `agent_energy_residual` | full | Zig ReleaseFast | 870.00 | 1360.00 | 0.181 | 21688 |
| `agent_energy_residual` | full | Python interpreted | 82139.00 | 202867.00 | 0.428 | 21688 |
| `agent_point_bounds` | small | S3 Pure O1 | 2388.75 | 6520.00 | 0.448 | 21688 |
| `agent_point_bounds` | small | S3 Per-instruction O1 | 2755.00 | 3651.25 | 0.213 | 21688 |
| `agent_point_bounds` | small | S3 Exact-segment O1 | 2780.00 | 4593.75 | 0.265 | 21688 |
| `agent_point_bounds` | small | S3 Loop-hybrid O1 | 3023.75 | 5753.75 | 0.272 | 21688 |
| `agent_point_bounds` | small | GCC O2 | 75.00 | 101.25 | 0.193 | 21688 |
| `agent_point_bounds` | small | Clang O2 | 65.00 | 212.50 | 0.530 | 21688 |
| `agent_point_bounds` | small | Rust opt-level 2 | 80.00 | 192.50 | 0.414 | 21688 |
| `agent_point_bounds` | small | Zig ReleaseFast | 88.75 | 142.50 | 0.213 | 21688 |
| `agent_point_bounds` | small | Python interpreted | 4879.88 | 11483.50 | 0.338 | 21688 |
| `agent_point_bounds` | medium | S3 Pure O1 | 9255.00 | 11840.00 | 0.254 | 21688 |
| `agent_point_bounds` | medium | S3 Per-instruction O1 | 9505.00 | 35535.00 | 0.538 | 21688 |
| `agent_point_bounds` | medium | S3 Exact-segment O1 | 10355.00 | 30414.50 | 0.536 | 21688 |
| `agent_point_bounds` | medium | S3 Loop-hybrid O1 | 8200.00 | 57525.00 | 1.110 | 21688 |
| `agent_point_bounds` | medium | GCC O2 | 280.00 | 490.00 | 0.293 | 21688 |
| `agent_point_bounds` | medium | Clang O2 | 200.00 | 300.00 | 0.166 | 21688 |
| `agent_point_bounds` | medium | Rust opt-level 2 | 275.00 | 645.00 | 0.369 | 21688 |
| `agent_point_bounds` | medium | Zig ReleaseFast | 305.00 | 475.00 | 0.199 | 21688 |
| `agent_point_bounds` | medium | Python interpreted | 17174.50 | 71024.00 | 0.675 | 21688 |
| `agent_point_bounds` | full | S3 Pure O1 | 15210.00 | 19390.00 | 0.185 | 21688 |
| `agent_point_bounds` | full | S3 Per-instruction O1 | 16600.00 | 19300.00 | 0.184 | 21688 |
| `agent_point_bounds` | full | S3 Exact-segment O1 | 16970.00 | 28570.00 | 0.298 | 21688 |
| `agent_point_bounds` | full | S3 Loop-hybrid O1 | 18660.00 | 130510.00 | 1.059 | 21688 |
| `agent_point_bounds` | full | GCC O2 | 430.00 | 570.00 | 0.177 | 21688 |
| `agent_point_bounds` | full | Clang O2 | 360.00 | 4990.00 | 1.562 | 21688 |
| `agent_point_bounds` | full | Rust opt-level 2 | 530.00 | 1510.00 | 0.513 | 21688 |
| `agent_point_bounds` | full | Zig ReleaseFast | 600.00 | 900.00 | 0.184 | 21688 |
| `agent_point_bounds` | full | Python interpreted | 31300.00 | 72758.00 | 0.396 | 21688 |
| `agent_raster_threshold_count` | small | S3 Pure O1 | 1756.25 | 35438.62 | 1.935 | 21688 |
| `agent_raster_threshold_count` | small | S3 Per-instruction O1 | 2081.25 | 2328.75 | 0.218 | 21688 |
| `agent_raster_threshold_count` | small | S3 Exact-segment O1 | 2167.50 | 3308.62 | 0.339 | 21688 |
| `agent_raster_threshold_count` | small | S3 Loop-hybrid O1 | 2201.25 | 2685.00 | 0.154 | 21688 |
| `agent_raster_threshold_count` | small | GCC O2 | 91.25 | 2048.75 | 2.127 | 21688 |
| `agent_raster_threshold_count` | small | Clang O2 | 147.50 | 222.50 | 0.175 | 21688 |
| `agent_raster_threshold_count` | small | Rust opt-level 2 | 122.50 | 175.00 | 0.168 | 21688 |
| `agent_raster_threshold_count` | small | Zig ReleaseFast | 70.00 | 125.00 | 0.323 | 21688 |
| `agent_raster_threshold_count` | small | Python interpreted | 2465.00 | 7519.88 | 0.564 | 21688 |
| `agent_raster_threshold_count` | medium | S3 Pure O1 | 5690.00 | 7275.00 | 0.234 | 21688 |
| `agent_raster_threshold_count` | medium | S3 Per-instruction O1 | 6565.00 | 9475.00 | 0.291 | 21688 |
| `agent_raster_threshold_count` | medium | S3 Exact-segment O1 | 6910.00 | 23045.00 | 0.548 | 21688 |
| `agent_raster_threshold_count` | medium | S3 Loop-hybrid O1 | 7420.00 | 24395.00 | 0.589 | 21688 |
| `agent_raster_threshold_count` | medium | GCC O2 | 285.00 | 1465.00 | 0.765 | 21688 |
| `agent_raster_threshold_count` | medium | Clang O2 | 570.00 | 890.00 | 0.230 | 21688 |
| `agent_raster_threshold_count` | medium | Rust opt-level 2 | 540.00 | 1055.00 | 0.271 | 21688 |
| `agent_raster_threshold_count` | medium | Zig ReleaseFast | 200.00 | 300.00 | 0.184 | 21688 |
| `agent_raster_threshold_count` | medium | Python interpreted | 9990.00 | 19145.00 | 0.371 | 21688 |
| `agent_raster_threshold_count` | full | S3 Pure O1 | 14340.00 | 17970.00 | 0.214 | 21688 |
| `agent_raster_threshold_count` | full | S3 Per-instruction O1 | 15070.00 | 107460.00 | 1.133 | 21688 |
| `agent_raster_threshold_count` | full | S3 Exact-segment O1 | 18680.00 | 24880.00 | 0.252 | 21688 |
| `agent_raster_threshold_count` | full | S3 Loop-hybrid O1 | 16730.00 | 101901.00 | 1.004 | 21688 |
| `agent_raster_threshold_count` | full | GCC O2 | 630.00 | 1360.00 | 0.358 | 21688 |
| `agent_raster_threshold_count` | full | Clang O2 | 1290.00 | 2160.00 | 0.312 | 21688 |
| `agent_raster_threshold_count` | full | Rust opt-level 2 | 1220.00 | 13380.00 | 1.510 | 21688 |
| `agent_raster_threshold_count` | full | Zig ReleaseFast | 610.00 | 1940.00 | 0.545 | 21688 |
| `agent_raster_threshold_count` | full | Python interpreted | 27360.00 | 63489.00 | 0.354 | 21688 |
| `agent_raster_valid_mean` | small | S3 Pure O1 | 2880.00 | 5322.50 | 0.291 | 21688 |
| `agent_raster_valid_mean` | small | S3 Per-instruction O1 | 3063.75 | 27564.38 | 1.308 | 21688 |
| `agent_raster_valid_mean` | small | S3 Exact-segment O1 | 2850.00 | 16912.50 | 0.902 | 21688 |
| `agent_raster_valid_mean` | small | S3 Loop-hybrid O1 | 3078.75 | 3797.50 | 0.183 | 21688 |
| `agent_raster_valid_mean` | small | GCC O2 | 98.75 | 138.75 | 0.173 | 21688 |
| `agent_raster_valid_mean` | small | Clang O2 | 90.00 | 153.75 | 0.212 | 21688 |
| `agent_raster_valid_mean` | small | Rust opt-level 2 | 103.75 | 307.50 | 0.497 | 21688 |
| `agent_raster_valid_mean` | small | Zig ReleaseFast | 117.50 | 182.50 | 0.200 | 21688 |
| `agent_raster_valid_mean` | small | Python interpreted | 4133.62 | 10498.12 | 0.467 | 21688 |
| `agent_raster_valid_mean` | medium | S3 Pure O1 | 10130.00 | 72810.00 | 1.056 | 21688 |
| `agent_raster_valid_mean` | medium | S3 Per-instruction O1 | 9715.00 | 31145.00 | 0.661 | 21688 |
| `agent_raster_valid_mean` | medium | S3 Exact-segment O1 | 10334.50 | 11965.00 | 0.245 | 21688 |
| `agent_raster_valid_mean` | medium | S3 Loop-hybrid O1 | 11060.00 | 19995.00 | 0.294 | 21688 |
| `agent_raster_valid_mean` | medium | GCC O2 | 330.00 | 760.00 | 0.399 | 21688 |
| `agent_raster_valid_mean` | medium | Clang O2 | 370.00 | 500.00 | 0.137 | 21688 |
| `agent_raster_valid_mean` | medium | Rust opt-level 2 | 375.00 | 780.00 | 0.334 | 21688 |
| `agent_raster_valid_mean` | medium | Zig ReleaseFast | 400.00 | 800.00 | 0.249 | 21688 |
| `agent_raster_valid_mean` | medium | Python interpreted | 15984.50 | 31354.50 | 0.315 | 21688 |
| `agent_raster_valid_mean` | full | S3 Pure O1 | 22820.00 | 35780.00 | 0.243 | 21688 |
| `agent_raster_valid_mean` | full | S3 Per-instruction O1 | 24870.00 | 30580.00 | 0.204 | 21688 |
| `agent_raster_valid_mean` | full | S3 Exact-segment O1 | 27170.00 | 56930.00 | 0.355 | 21688 |
| `agent_raster_valid_mean` | full | S3 Loop-hybrid O1 | 31030.00 | 109850.00 | 0.689 | 21688 |
| `agent_raster_valid_mean` | full | GCC O2 | 990.00 | 2010.00 | 0.365 | 21688 |
| `agent_raster_valid_mean` | full | Clang O2 | 930.00 | 1290.00 | 0.177 | 21688 |
| `agent_raster_valid_mean` | full | Rust opt-level 2 | 860.00 | 1160.00 | 0.156 | 21688 |
| `agent_raster_valid_mean` | full | Zig ReleaseFast | 950.00 | 2160.00 | 0.335 | 21688 |
| `agent_raster_valid_mean` | full | Python interpreted | 45750.00 | 61459.00 | 0.263 | 21688 |
| `energy_series_aggregation` | small | S3 Pure O1 | 3858.75 | 5741.25 | 0.212 | 21688 |
| `energy_series_aggregation` | small | S3 Per-instruction O1 | 4558.75 | 8323.75 | 0.284 | 21688 |
| `energy_series_aggregation` | small | S3 Exact-segment O1 | 4746.25 | 22837.50 | 0.796 | 21688 |
| `energy_series_aggregation` | small | S3 Loop-hybrid O1 | 4635.00 | 5845.00 | 0.214 | 21688 |
| `energy_series_aggregation` | small | GCC O2 | 102.50 | 131.25 | 0.149 | 21688 |
| `energy_series_aggregation` | small | Clang O2 | 112.50 | 175.00 | 0.206 | 21688 |
| `energy_series_aggregation` | small | Rust opt-level 2 | 102.50 | 242.50 | 0.365 | 21688 |
| `energy_series_aggregation` | small | Zig ReleaseFast | 101.25 | 151.25 | 0.180 | 21688 |
| `energy_series_aggregation` | small | Python interpreted | 8091.12 | 14428.50 | 0.297 | 21688 |
| `energy_series_aggregation` | medium | S3 Pure O1 | 16900.00 | 24920.00 | 0.182 | 21688 |
| `energy_series_aggregation` | medium | S3 Per-instruction O1 | 16210.00 | 21825.00 | 0.210 | 21688 |
| `energy_series_aggregation` | medium | S3 Exact-segment O1 | 16425.00 | 19825.00 | 0.143 | 21688 |
| `energy_series_aggregation` | medium | S3 Loop-hybrid O1 | 17080.00 | 21840.00 | 0.272 | 21688 |
| `energy_series_aggregation` | medium | GCC O2 | 465.00 | 715.00 | 0.210 | 21688 |
| `energy_series_aggregation` | medium | Clang O2 | 460.00 | 570.00 | 0.168 | 21688 |
| `energy_series_aggregation` | medium | Rust opt-level 2 | 410.00 | 665.00 | 0.208 | 21688 |
| `energy_series_aggregation` | medium | Zig ReleaseFast | 340.00 | 420.00 | 0.118 | 21688 |
| `energy_series_aggregation` | medium | Python interpreted | 28234.50 | 42909.50 | 0.186 | 21688 |
| `energy_series_aggregation` | full | S3 Pure O1 | 42620.00 | 85480.00 | 0.284 | 21688 |
| `energy_series_aggregation` | full | S3 Per-instruction O1 | 49110.00 | 90969.00 | 0.296 | 21688 |
| `energy_series_aggregation` | full | S3 Exact-segment O1 | 47010.00 | 189050.00 | 0.699 | 21688 |
| `energy_series_aggregation` | full | S3 Loop-hybrid O1 | 48110.00 | 81200.00 | 0.299 | 21688 |
| `energy_series_aggregation` | full | GCC O2 | 850.00 | 156969.00 | 3.431 | 21688 |
| `energy_series_aggregation` | full | Clang O2 | 970.00 | 1700.00 | 0.264 | 21688 |
| `energy_series_aggregation` | full | Rust opt-level 2 | 1010.00 | 1810.00 | 0.273 | 21688 |
| `energy_series_aggregation` | full | Zig ReleaseFast | 800.00 | 3160.00 | 0.623 | 21688 |
| `energy_series_aggregation` | full | Python interpreted | 75489.00 | 206847.00 | 0.433 | 21688 |
| `point_cloud_summary` | small | S3 Pure O1 | 5182.50 | 6108.75 | 0.137 | 21688 |
| `point_cloud_summary` | small | S3 Per-instruction O1 | 5709.88 | 6606.25 | 0.155 | 21688 |
| `point_cloud_summary` | small | S3 Exact-segment O1 | 5496.25 | 6955.00 | 0.287 | 21688 |
| `point_cloud_summary` | small | S3 Loop-hybrid O1 | 5567.50 | 18123.12 | 0.596 | 21688 |
| `point_cloud_summary` | small | GCC O2 | 130.00 | 321.25 | 0.415 | 21688 |
| `point_cloud_summary` | small | Clang O2 | 107.50 | 131.25 | 0.138 | 21688 |
| `point_cloud_summary` | small | Rust opt-level 2 | 126.25 | 140.00 | 0.114 | 21688 |
| `point_cloud_summary` | small | Zig ReleaseFast | 122.50 | 170.00 | 0.173 | 21688 |
| `point_cloud_summary` | small | Python interpreted | 13743.50 | 26277.12 | 0.268 | 21688 |
| `point_cloud_summary` | medium | S3 Pure O1 | 19460.00 | 26840.00 | 0.250 | 21688 |
| `point_cloud_summary` | medium | S3 Per-instruction O1 | 20439.50 | 22815.00 | 0.241 | 21688 |
| `point_cloud_summary` | medium | S3 Exact-segment O1 | 17810.00 | 48530.00 | 0.476 | 21688 |
| `point_cloud_summary` | medium | S3 Loop-hybrid O1 | 18950.00 | 23650.00 | 0.295 | 21688 |
| `point_cloud_summary` | medium | GCC O2 | 435.00 | 1560.00 | 0.608 | 21688 |
| `point_cloud_summary` | medium | Clang O2 | 375.00 | 910.00 | 0.362 | 21688 |
| `point_cloud_summary` | medium | Rust opt-level 2 | 445.00 | 775.00 | 0.288 | 21688 |
| `point_cloud_summary` | medium | Zig ReleaseFast | 465.00 | 575.00 | 0.118 | 21688 |
| `point_cloud_summary` | medium | Python interpreted | 46104.00 | 141417.50 | 0.467 | 21688 |
| `point_cloud_summary` | full | S3 Pure O1 | 30680.00 | 36920.00 | 0.211 | 21688 |
| `point_cloud_summary` | full | S3 Per-instruction O1 | 36750.00 | 138879.00 | 0.669 | 21688 |
| `point_cloud_summary` | full | S3 Exact-segment O1 | 36260.00 | 90421.00 | 0.413 | 21688 |
| `point_cloud_summary` | full | S3 Loop-hybrid O1 | 36650.00 | 126140.00 | 0.605 | 21688 |
| `point_cloud_summary` | full | GCC O2 | 720.00 | 1060.00 | 0.174 | 21688 |
| `point_cloud_summary` | full | Clang O2 | 670.00 | 1330.00 | 0.266 | 21688 |
| `point_cloud_summary` | full | Rust opt-level 2 | 800.00 | 1010.00 | 0.193 | 21688 |
| `point_cloud_summary` | full | Zig ReleaseFast | 940.00 | 1530.00 | 0.258 | 21688 |
| `point_cloud_summary` | full | Python interpreted | 79679.00 | 106788.00 | 0.240 | 21688 |

## Process initialization and peak memory

Initialization is measured in separate zero-iteration launches after one untimed correctness call; it includes spawn, loader/interpreter and fixture decoding. It is not subtracted from the kernel timer.

| Workload | Input | Implementation | Median wall ns | p95 wall ns |
|---|---:|---|---:|---:|
| `agent_energy_residual` | full | Clang `O0/O0` | 6369230 | 6561017 |
| `agent_energy_residual` | full | Clang `O2/O2` | 7739498 | 7991885 |
| `agent_energy_residual` | full | GCC `O0/O0` | 9382653 | 10969408 |
| `agent_energy_residual` | full | GCC `O2/O2` | 8513666 | 9778895 |
| `agent_energy_residual` | full | Python `CPython/interpreted` | 91612765 | 102380581 |
| `agent_energy_residual` | full | Rust `opt-level-0/opt-level-0` | 6785623 | 7363684 |
| `agent_energy_residual` | full | Rust `opt-level-2/opt-level-2` | 6257022 | 6515732 |
| `agent_energy_residual` | full | S3 `EXACT_SEGMENT/O0` | 5282956 | 5395322 |
| `agent_energy_residual` | full | S3 `EXACT_SEGMENT/O1` | 6001895 | 6114764 |
| `agent_energy_residual` | full | S3 `LOOP_HYBRID/O0` | 7023314 | 8998004 |
| `agent_energy_residual` | full | S3 `LOOP_HYBRID/O1` | 6187522 | 6714245 |
| `agent_energy_residual` | full | S3 `PER_INSTRUCTION/O0` | 6193498 | 7798617 |
| `agent_energy_residual` | full | S3 `PER_INSTRUCTION/O1` | 8541105 | 8801247 |
| `agent_energy_residual` | full | S3 `PURE_EXPERIMENTAL/O0` | 5724871 | 6197093 |
| `agent_energy_residual` | full | S3 `PURE_EXPERIMENTAL/O1` | 5596772 | 7510272 |
| `agent_energy_residual` | full | Zig `Debug/Debug` | 7221516 | 8049268 |
| `agent_energy_residual` | full | Zig `ReleaseFast/ReleaseFast` | 9115162 | 9569614 |
| `agent_energy_residual` | medium | Clang `O0/O0` | 6390250 | 6583116 |
| `agent_energy_residual` | medium | Clang `O2/O2` | 7180412 | 7419209 |
| `agent_energy_residual` | medium | GCC `O0/O0` | 10475086 | 10918679 |
| `agent_energy_residual` | medium | GCC `O2/O2` | 10660318 | 12134705 |
| `agent_energy_residual` | medium | Python `CPython/interpreted` | 66540849 | 92524976 |
| `agent_energy_residual` | medium | Rust `opt-level-0/opt-level-0` | 7480422 | 7557131 |
| `agent_energy_residual` | medium | Rust `opt-level-2/opt-level-2` | 7697724 | 8198912 |
| `agent_energy_residual` | medium | S3 `EXACT_SEGMENT/O0` | 5031751 | 5374885 |
| `agent_energy_residual` | medium | S3 `EXACT_SEGMENT/O1` | 6711799 | 7309985 |
| `agent_energy_residual` | medium | S3 `LOOP_HYBRID/O0` | 6592736 | 7622965 |
| `agent_energy_residual` | medium | S3 `LOOP_HYBRID/O1` | 5954526 | 7359724 |
| `agent_energy_residual` | medium | S3 `PER_INSTRUCTION/O0` | 5399295 | 7497712 |
| `agent_energy_residual` | medium | S3 `PER_INSTRUCTION/O1` | 7056499 | 7350254 |
| `agent_energy_residual` | medium | S3 `PURE_EXPERIMENTAL/O0` | 5419250 | 6318656 |
| `agent_energy_residual` | medium | S3 `PURE_EXPERIMENTAL/O1` | 5464095 | 6326571 |
| `agent_energy_residual` | medium | Zig `Debug/Debug` | 6059190 | 6373850 |
| `agent_energy_residual` | medium | Zig `ReleaseFast/ReleaseFast` | 9367087 | 10468441 |
| `agent_energy_residual` | small | Clang `O0/O0` | 6219072 | 6247182 |
| `agent_energy_residual` | small | Clang `O2/O2` | 6180783 | 7182396 |
| `agent_energy_residual` | small | GCC `O0/O0` | 7296740 | 8500911 |
| `agent_energy_residual` | small | GCC `O2/O2` | 11063702 | 11400815 |
| `agent_energy_residual` | small | Python `CPython/interpreted` | 66279204 | 84659435 |
| `agent_energy_residual` | small | Rust `opt-level-0/opt-level-0` | 8267420 | 8704339 |
| `agent_energy_residual` | small | Rust `opt-level-2/opt-level-2` | 6897902 | 8040894 |
| `agent_energy_residual` | small | S3 `EXACT_SEGMENT/O0` | 5082290 | 5285537 |
| `agent_energy_residual` | small | S3 `EXACT_SEGMENT/O1` | 7485277 | 8197281 |
| `agent_energy_residual` | small | S3 `LOOP_HYBRID/O0` | 6621596 | 6755434 |
| `agent_energy_residual` | small | S3 `LOOP_HYBRID/O1` | 6449659 | 7334860 |
| `agent_energy_residual` | small | S3 `PER_INSTRUCTION/O0` | 5529983 | 5652521 |
| `agent_energy_residual` | small | S3 `PER_INSTRUCTION/O1` | 7026905 | 7640364 |
| `agent_energy_residual` | small | S3 `PURE_EXPERIMENTAL/O0` | 7836186 | 8043239 |
| `agent_energy_residual` | small | S3 `PURE_EXPERIMENTAL/O1` | 5262047 | 5768860 |
| `agent_energy_residual` | small | Zig `Debug/Debug` | 7053204 | 8427572 |
| `agent_energy_residual` | small | Zig `ReleaseFast/ReleaseFast` | 9580850 | 10676607 |
| `agent_point_bounds` | full | Clang `O0/O0` | 7258680 | 7327145 |
| `agent_point_bounds` | full | Clang `O2/O2` | 6092594 | 6096695 |
| `agent_point_bounds` | full | GCC `O0/O0` | 9267915 | 9931099 |
| `agent_point_bounds` | full | GCC `O2/O2` | 8800907 | 9230720 |
| `agent_point_bounds` | full | Python `CPython/interpreted` | 88343976 | 93618467 |
| `agent_point_bounds` | full | Rust `opt-level-0/opt-level-0` | 6434069 | 8511401 |
| `agent_point_bounds` | full | Rust `opt-level-2/opt-level-2` | 7011480 | 7603956 |
| `agent_point_bounds` | full | S3 `EXACT_SEGMENT/O0` | 8649644 | 10713922 |
| `agent_point_bounds` | full | S3 `EXACT_SEGMENT/O1` | 7565707 | 11231827 |
| `agent_point_bounds` | full | S3 `LOOP_HYBRID/O0` | 7250611 | 7887182 |
| `agent_point_bounds` | full | S3 `LOOP_HYBRID/O1` | 7387924 | 7540236 |
| `agent_point_bounds` | full | S3 `PER_INSTRUCTION/O0` | 8623064 | 9261119 |
| `agent_point_bounds` | full | S3 `PER_INSTRUCTION/O1` | 8212296 | 10903699 |
| `agent_point_bounds` | full | S3 `PURE_EXPERIMENTAL/O0` | 8174781 | 8522245 |
| `agent_point_bounds` | full | S3 `PURE_EXPERIMENTAL/O1` | 8822761 | 9825235 |
| `agent_point_bounds` | full | Zig `Debug/Debug` | 8469818 | 9703712 |
| `agent_point_bounds` | full | Zig `ReleaseFast/ReleaseFast` | 8008734 | 8397898 |
| `agent_point_bounds` | medium | Clang `O0/O0` | 7221526 | 7561472 |
| `agent_point_bounds` | medium | Clang `O2/O2` | 7605206 | 9517635 |
| `agent_point_bounds` | medium | GCC `O0/O0` | 7848152 | 10372427 |
| `agent_point_bounds` | medium | GCC `O2/O2` | 9107532 | 10377181 |
| `agent_point_bounds` | medium | Python `CPython/interpreted` | 100243624 | 107585204 |
| `agent_point_bounds` | medium | Rust `opt-level-0/opt-level-0` | 6646151 | 7897771 |
| `agent_point_bounds` | medium | Rust `opt-level-2/opt-level-2` | 6686825 | 6996870 |
| `agent_point_bounds` | medium | S3 `EXACT_SEGMENT/O0` | 9198045 | 9667088 |
| `agent_point_bounds` | medium | S3 `EXACT_SEGMENT/O1` | 7796068 | 8739923 |
| `agent_point_bounds` | medium | S3 `LOOP_HYBRID/O0` | 7952966 | 7998289 |
| `agent_point_bounds` | medium | S3 `LOOP_HYBRID/O1` | 7345040 | 8372889 |
| `agent_point_bounds` | medium | S3 `PER_INSTRUCTION/O0` | 9075057 | 9338563 |
| `agent_point_bounds` | medium | S3 `PER_INSTRUCTION/O1` | 6770523 | 11423150 |
| `agent_point_bounds` | medium | S3 `PURE_EXPERIMENTAL/O0` | 8079102 | 8428588 |
| `agent_point_bounds` | medium | S3 `PURE_EXPERIMENTAL/O1` | 7116544 | 7717614 |
| `agent_point_bounds` | medium | Zig `Debug/Debug` | 7226917 | 8580245 |
| `agent_point_bounds` | medium | Zig `ReleaseFast/ReleaseFast` | 7063744 | 7647740 |
| `agent_point_bounds` | small | Clang `O0/O0` | 6517423 | 6554982 |
| `agent_point_bounds` | small | Clang `O2/O2` | 6822743 | 7742849 |
| `agent_point_bounds` | small | GCC `O0/O0` | 8656760 | 8802340 |
| `agent_point_bounds` | small | GCC `O2/O2` | 10251914 | 10595354 |
| `agent_point_bounds` | small | Python `CPython/interpreted` | 93200730 | 96484343 |
| `agent_point_bounds` | small | Rust `opt-level-0/opt-level-0` | 7770523 | 8163592 |
| `agent_point_bounds` | small | Rust `opt-level-2/opt-level-2` | 6468128 | 6553337 |
| `agent_point_bounds` | small | S3 `EXACT_SEGMENT/O0` | 8612574 | 9519321 |
| `agent_point_bounds` | small | S3 `EXACT_SEGMENT/O1` | 8344529 | 9408903 |
| `agent_point_bounds` | small | S3 `LOOP_HYBRID/O0` | 6844917 | 7484533 |
| `agent_point_bounds` | small | S3 `LOOP_HYBRID/O1` | 6114664 | 7528362 |
| `agent_point_bounds` | small | S3 `PER_INSTRUCTION/O0` | 9348108 | 12524473 |
| `agent_point_bounds` | small | S3 `PER_INSTRUCTION/O1` | 8726673 | 10035312 |
| `agent_point_bounds` | small | S3 `PURE_EXPERIMENTAL/O0` | 6417299 | 7645750 |
| `agent_point_bounds` | small | S3 `PURE_EXPERIMENTAL/O1` | 8307834 | 9923039 |
| `agent_point_bounds` | small | Zig `Debug/Debug` | 8202961 | 9367073 |
| `agent_point_bounds` | small | Zig `ReleaseFast/ReleaseFast` | 7478268 | 7939986 |
| `agent_raster_threshold_count` | full | Clang `O0/O0` | 6658010 | 7173262 |
| `agent_raster_threshold_count` | full | Clang `O2/O2` | 7646699 | 9064103 |
| `agent_raster_threshold_count` | full | GCC `O0/O0` | 9169991 | 10521769 |
| `agent_raster_threshold_count` | full | GCC `O2/O2` | 9007143 | 10305018 |
| `agent_raster_threshold_count` | full | Python `CPython/interpreted` | 80983922 | 102672138 |
| `agent_raster_threshold_count` | full | Rust `opt-level-0/opt-level-0` | 6697449 | 7071459 |
| `agent_raster_threshold_count` | full | Rust `opt-level-2/opt-level-2` | 7262796 | 7935810 |
| `agent_raster_threshold_count` | full | S3 `EXACT_SEGMENT/O0` | 8097348 | 8975239 |
| `agent_raster_threshold_count` | full | S3 `EXACT_SEGMENT/O1` | 8816256 | 9377753 |
| `agent_raster_threshold_count` | full | S3 `LOOP_HYBRID/O0` | 9498806 | 9951623 |
| `agent_raster_threshold_count` | full | S3 `LOOP_HYBRID/O1` | 9002324 | 9007318 |
| `agent_raster_threshold_count` | full | S3 `PER_INSTRUCTION/O0` | 8638285 | 8713618 |
| `agent_raster_threshold_count` | full | S3 `PER_INSTRUCTION/O1` | 8613521 | 9854590 |
| `agent_raster_threshold_count` | full | S3 `PURE_EXPERIMENTAL/O0` | 7084075 | 7212716 |
| `agent_raster_threshold_count` | full | S3 `PURE_EXPERIMENTAL/O1` | 6089525 | 6156683 |
| `agent_raster_threshold_count` | full | Zig `Debug/Debug` | 7576681 | 8710518 |
| `agent_raster_threshold_count` | full | Zig `ReleaseFast/ReleaseFast` | 5566122 | 6209613 |
| `agent_raster_threshold_count` | medium | Clang `O0/O0` | 6475924 | 6672965 |
| `agent_raster_threshold_count` | medium | Clang `O2/O2` | 6940321 | 8456902 |
| `agent_raster_threshold_count` | medium | GCC `O0/O0` | 9285979 | 9810547 |
| `agent_raster_threshold_count` | medium | GCC `O2/O2` | 8202431 | 9768536 |
| `agent_raster_threshold_count` | medium | Python `CPython/interpreted` | 77132183 | 80878709 |
| `agent_raster_threshold_count` | medium | Rust `opt-level-0/opt-level-0` | 6603396 | 8180236 |
| `agent_raster_threshold_count` | medium | Rust `opt-level-2/opt-level-2` | 6950345 | 7253486 |
| `agent_raster_threshold_count` | medium | S3 `EXACT_SEGMENT/O0` | 7483592 | 8098683 |
| `agent_raster_threshold_count` | medium | S3 `EXACT_SEGMENT/O1` | 8334244 | 9079383 |
| `agent_raster_threshold_count` | medium | S3 `LOOP_HYBRID/O0` | 8726997 | 9867571 |
| `agent_raster_threshold_count` | medium | S3 `LOOP_HYBRID/O1` | 8340670 | 8527035 |
| `agent_raster_threshold_count` | medium | S3 `PER_INSTRUCTION/O0` | 7289252 | 7541546 |
| `agent_raster_threshold_count` | medium | S3 `PER_INSTRUCTION/O1` | 8946769 | 9419997 |
| `agent_raster_threshold_count` | medium | S3 `PURE_EXPERIMENTAL/O0` | 6470327 | 8346909 |
| `agent_raster_threshold_count` | medium | S3 `PURE_EXPERIMENTAL/O1` | 7285415 | 7340509 |
| `agent_raster_threshold_count` | medium | Zig `Debug/Debug` | 8905411 | 9947809 |
| `agent_raster_threshold_count` | medium | Zig `ReleaseFast/ReleaseFast` | 6001945 | 6195192 |
| `agent_raster_threshold_count` | small | Clang `O0/O0` | 7195122 | 8650810 |
| `agent_raster_threshold_count` | small | Clang `O2/O2` | 7688794 | 7976210 |
| `agent_raster_threshold_count` | small | GCC `O0/O0` | 8287405 | 8750192 |
| `agent_raster_threshold_count` | small | GCC `O2/O2` | 7973729 | 8292805 |
| `agent_raster_threshold_count` | small | Python `CPython/interpreted` | 90906796 | 96349016 |
| `agent_raster_threshold_count` | small | Rust `opt-level-0/opt-level-0` | 7501622 | 7572040 |
| `agent_raster_threshold_count` | small | Rust `opt-level-2/opt-level-2` | 6909637 | 8067763 |
| `agent_raster_threshold_count` | small | S3 `EXACT_SEGMENT/O0` | 7876556 | 8152531 |
| `agent_raster_threshold_count` | small | S3 `EXACT_SEGMENT/O1` | 9604885 | 9930384 |
| `agent_raster_threshold_count` | small | S3 `LOOP_HYBRID/O0` | 8582439 | 9104372 |
| `agent_raster_threshold_count` | small | S3 `LOOP_HYBRID/O1` | 9111421 | 9320749 |
| `agent_raster_threshold_count` | small | S3 `PER_INSTRUCTION/O0` | 7546872 | 8962333 |
| `agent_raster_threshold_count` | small | S3 `PER_INSTRUCTION/O1` | 8354344 | 8983869 |
| `agent_raster_threshold_count` | small | S3 `PURE_EXPERIMENTAL/O0` | 7186612 | 9412192 |
| `agent_raster_threshold_count` | small | S3 `PURE_EXPERIMENTAL/O1` | 6786714 | 7757743 |
| `agent_raster_threshold_count` | small | Zig `Debug/Debug` | 8187922 | 9300910 |
| `agent_raster_threshold_count` | small | Zig `ReleaseFast/ReleaseFast` | 7487568 | 8627003 |
| `agent_raster_valid_mean` | full | Clang `O0/O0` | 7895936 | 8135647 |
| `agent_raster_valid_mean` | full | Clang `O2/O2` | 6876107 | 8273875 |
| `agent_raster_valid_mean` | full | GCC `O0/O0` | 7370550 | 7597785 |
| `agent_raster_valid_mean` | full | GCC `O2/O2` | 6650626 | 7554758 |
| `agent_raster_valid_mean` | full | Python `CPython/interpreted` | 78751402 | 80275073 |
| `agent_raster_valid_mean` | full | Rust `opt-level-0/opt-level-0` | 8041694 | 8453077 |
| `agent_raster_valid_mean` | full | Rust `opt-level-2/opt-level-2` | 7394729 | 9212975 |
| `agent_raster_valid_mean` | full | S3 `EXACT_SEGMENT/O0` | 8211081 | 8777317 |
| `agent_raster_valid_mean` | full | S3 `EXACT_SEGMENT/O1` | 8683104 | 8786686 |
| `agent_raster_valid_mean` | full | S3 `LOOP_HYBRID/O0` | 9275394 | 9409718 |
| `agent_raster_valid_mean` | full | S3 `LOOP_HYBRID/O1` | 8927400 | 10702682 |
| `agent_raster_valid_mean` | full | S3 `PER_INSTRUCTION/O0` | 8316889 | 8467206 |
| `agent_raster_valid_mean` | full | S3 `PER_INSTRUCTION/O1` | 8607805 | 8848261 |
| `agent_raster_valid_mean` | full | S3 `PURE_EXPERIMENTAL/O0` | 7983825 | 8068408 |
| `agent_raster_valid_mean` | full | S3 `PURE_EXPERIMENTAL/O1` | 8260319 | 8460307 |
| `agent_raster_valid_mean` | full | Zig `Debug/Debug` | 6015355 | 7423424 |
| `agent_raster_valid_mean` | full | Zig `ReleaseFast/ReleaseFast` | 6115154 | 7670810 |
| `agent_raster_valid_mean` | medium | Clang `O0/O0` | 7504817 | 7937081 |
| `agent_raster_valid_mean` | medium | Clang `O2/O2` | 8341038 | 8391604 |
| `agent_raster_valid_mean` | medium | GCC `O0/O0` | 8742492 | 10572433 |
| `agent_raster_valid_mean` | medium | GCC `O2/O2` | 7174127 | 7198252 |
| `agent_raster_valid_mean` | medium | Python `CPython/interpreted` | 103170094 | 120667828 |
| `agent_raster_valid_mean` | medium | Rust `opt-level-0/opt-level-0` | 6648261 | 7282981 |
| `agent_raster_valid_mean` | medium | Rust `opt-level-2/opt-level-2` | 7630755 | 8971689 |
| `agent_raster_valid_mean` | medium | S3 `EXACT_SEGMENT/O0` | 8694803 | 8778882 |
| `agent_raster_valid_mean` | medium | S3 `EXACT_SEGMENT/O1` | 10177011 | 10493890 |
| `agent_raster_valid_mean` | medium | S3 `LOOP_HYBRID/O0` | 8974199 | 9697748 |
| `agent_raster_valid_mean` | medium | S3 `LOOP_HYBRID/O1` | 8921825 | 8975244 |
| `agent_raster_valid_mean` | medium | S3 `PER_INSTRUCTION/O0` | 8680503 | 9121717 |
| `agent_raster_valid_mean` | medium | S3 `PER_INSTRUCTION/O1` | 8492082 | 9152326 |
| `agent_raster_valid_mean` | medium | S3 `PURE_EXPERIMENTAL/O0` | 7995419 | 8860481 |
| `agent_raster_valid_mean` | medium | S3 `PURE_EXPERIMENTAL/O1` | 8226665 | 8429798 |
| `agent_raster_valid_mean` | medium | Zig `Debug/Debug` | 6219382 | 6317611 |
| `agent_raster_valid_mean` | medium | Zig `ReleaseFast/ReleaseFast` | 6572351 | 7819667 |
| `agent_raster_valid_mean` | small | Clang `O0/O0` | 7479468 | 8439493 |
| `agent_raster_valid_mean` | small | Clang `O2/O2` | 7669400 | 7884686 |
| `agent_raster_valid_mean` | small | GCC `O0/O0` | 8659789 | 11533279 |
| `agent_raster_valid_mean` | small | GCC `O2/O2` | 7445633 | 8169487 |
| `agent_raster_valid_mean` | small | Python `CPython/interpreted` | 76233152 | 88852218 |
| `agent_raster_valid_mean` | small | Rust `opt-level-0/opt-level-0` | 6496353 | 6655395 |
| `agent_raster_valid_mean` | small | Rust `opt-level-2/opt-level-2` | 8134522 | 8596265 |
| `agent_raster_valid_mean` | small | S3 `EXACT_SEGMENT/O0` | 9385247 | 9632044 |
| `agent_raster_valid_mean` | small | S3 `EXACT_SEGMENT/O1` | 8490862 | 8792822 |
| `agent_raster_valid_mean` | small | S3 `LOOP_HYBRID/O0` | 8772742 | 9089353 |
| `agent_raster_valid_mean` | small | S3 `LOOP_HYBRID/O1` | 8596100 | 8764718 |
| `agent_raster_valid_mean` | small | S3 `PER_INSTRUCTION/O0` | 8603805 | 8641798 |
| `agent_raster_valid_mean` | small | S3 `PER_INSTRUCTION/O1` | 8028604 | 8181711 |
| `agent_raster_valid_mean` | small | S3 `PURE_EXPERIMENTAL/O0` | 8402063 | 11027142 |
| `agent_raster_valid_mean` | small | S3 `PURE_EXPERIMENTAL/O1` | 7846097 | 8348509 |
| `agent_raster_valid_mean` | small | Zig `Debug/Debug` | 6422899 | 6505018 |
| `agent_raster_valid_mean` | small | Zig `ReleaseFast/ReleaseFast` | 6001546 | 6520218 |
| `energy_series_aggregation` | full | Clang `O0/O0` | 8518691 | 8986550 |
| `energy_series_aggregation` | full | Clang `O2/O2` | 7148087 | 7856402 |
| `energy_series_aggregation` | full | GCC `O0/O0` | 8297320 | 10760601 |
| `energy_series_aggregation` | full | GCC `O2/O2` | 8413882 | 8581305 |
| `energy_series_aggregation` | full | Python `CPython/interpreted` | 79793006 | 86948608 |
| `energy_series_aggregation` | full | Rust `opt-level-0/opt-level-0` | 8269026 | 9464722 |
| `energy_series_aggregation` | full | Rust `opt-level-2/opt-level-2` | 8738637 | 9600093 |
| `energy_series_aggregation` | full | S3 `EXACT_SEGMENT/O0` | 9347178 | 9385803 |
| `energy_series_aggregation` | full | S3 `EXACT_SEGMENT/O1` | 10473371 | 13103649 |
| `energy_series_aggregation` | full | S3 `LOOP_HYBRID/O0` | 8295510 | 8964180 |
| `energy_series_aggregation` | full | S3 `LOOP_HYBRID/O1` | 9244305 | 10670797 |
| `energy_series_aggregation` | full | S3 `PER_INSTRUCTION/O0` | 9119432 | 10443937 |
| `energy_series_aggregation` | full | S3 `PER_INSTRUCTION/O1` | 8775672 | 9023408 |
| `energy_series_aggregation` | full | S3 `PURE_EXPERIMENTAL/O0` | 9021858 | 10050987 |
| `energy_series_aggregation` | full | S3 `PURE_EXPERIMENTAL/O1` | 9458041 | 10724381 |
| `energy_series_aggregation` | full | Zig `Debug/Debug` | 8646849 | 8676209 |
| `energy_series_aggregation` | full | Zig `ReleaseFast/ReleaseFast` | 7253336 | 7371834 |
| `energy_series_aggregation` | medium | Clang `O0/O0` | 7175727 | 7241811 |
| `energy_series_aggregation` | medium | Clang `O2/O2` | 7623145 | 8022284 |
| `energy_series_aggregation` | medium | GCC `O0/O0` | 8437464 | 9109153 |
| `energy_series_aggregation` | medium | GCC `O2/O2` | 8349919 | 9893669 |
| `energy_series_aggregation` | medium | Python `CPython/interpreted` | 74829069 | 75449574 |
| `energy_series_aggregation` | medium | Rust `opt-level-0/opt-level-0` | 9585625 | 9949498 |
| `energy_series_aggregation` | medium | Rust `opt-level-2/opt-level-2` | 8096033 | 9796406 |
| `energy_series_aggregation` | medium | S3 `EXACT_SEGMENT/O0` | 9746053 | 9947053 |
| `energy_series_aggregation` | medium | S3 `EXACT_SEGMENT/O1` | 12396746 | 14339314 |
| `energy_series_aggregation` | medium | S3 `LOOP_HYBRID/O0` | 8667258 | 9274960 |
| `energy_series_aggregation` | medium | S3 `LOOP_HYBRID/O1` | 9223370 | 9782811 |
| `energy_series_aggregation` | medium | S3 `PER_INSTRUCTION/O0` | 9107727 | 9185810 |
| `energy_series_aggregation` | medium | S3 `PER_INSTRUCTION/O1` | 9512130 | 9809255 |
| `energy_series_aggregation` | medium | S3 `PURE_EXPERIMENTAL/O0` | 7612970 | 8427618 |
| `energy_series_aggregation` | medium | S3 `PURE_EXPERIMENTAL/O1` | 8685618 | 9397007 |
| `energy_series_aggregation` | medium | Zig `Debug/Debug` | 6163799 | 8425923 |
| `energy_series_aggregation` | medium | Zig `ReleaseFast/ReleaseFast` | 7478584 | 7675059 |
| `energy_series_aggregation` | small | Clang `O0/O0` | 7613886 | 8720732 |
| `energy_series_aggregation` | small | Clang `O2/O2` | 8212415 | 8469462 |
| `energy_series_aggregation` | small | GCC `O0/O0` | 7601981 | 7929855 |
| `energy_series_aggregation` | small | GCC `O2/O2` | 7434988 | 7798938 |
| `energy_series_aggregation` | small | Python `CPython/interpreted` | 69684359 | 88770465 |
| `energy_series_aggregation` | small | Rust `opt-level-0/opt-level-0` | 8232825 | 10110927 |
| `energy_series_aggregation` | small | Rust `opt-level-2/opt-level-2` | 7268027 | 7295365 |
| `energy_series_aggregation` | small | S3 `EXACT_SEGMENT/O0` | 9022538 | 9092692 |
| `energy_series_aggregation` | small | S3 `EXACT_SEGMENT/O1` | 10501911 | 15401878 |
| `energy_series_aggregation` | small | S3 `LOOP_HYBRID/O0` | 9126606 | 9231836 |
| `energy_series_aggregation` | small | S3 `LOOP_HYBRID/O1` | 8679154 | 9913709 |
| `energy_series_aggregation` | small | S3 `PER_INSTRUCTION/O0` | 9538140 | 9652598 |
| `energy_series_aggregation` | small | S3 `PER_INSTRUCTION/O1` | 8885220 | 8971170 |
| `energy_series_aggregation` | small | S3 `PURE_EXPERIMENTAL/O0` | 8106182 | 9374732 |
| `energy_series_aggregation` | small | S3 `PURE_EXPERIMENTAL/O1` | 8632194 | 9745472 |
| `energy_series_aggregation` | small | Zig `Debug/Debug` | 6499938 | 6715540 |
| `energy_series_aggregation` | small | Zig `ReleaseFast/ReleaseFast` | 8747887 | 9010208 |
| `point_cloud_summary` | full | Clang `O0/O0` | 6463137 | 6840198 |
| `point_cloud_summary` | full | Clang `O2/O2` | 7482317 | 7835703 |
| `point_cloud_summary` | full | GCC `O0/O0` | 6610446 | 8767977 |
| `point_cloud_summary` | full | GCC `O2/O2` | 6278481 | 6280921 |
| `point_cloud_summary` | full | Python `CPython/interpreted` | 77523847 | 81445999 |
| `point_cloud_summary` | full | Rust `opt-level-0/opt-level-0` | 5847163 | 6303417 |
| `point_cloud_summary` | full | Rust `opt-level-2/opt-level-2` | 6430449 | 6460558 |
| `point_cloud_summary` | full | S3 `EXACT_SEGMENT/O0` | 10005578 | 12809108 |
| `point_cloud_summary` | full | S3 `EXACT_SEGMENT/O1` | 10343917 | 10698071 |
| `point_cloud_summary` | full | S3 `LOOP_HYBRID/O0` | 7524777 | 9688562 |
| `point_cloud_summary` | full | S3 `LOOP_HYBRID/O1` | 8686313 | 8708973 |
| `point_cloud_summary` | full | S3 `PER_INSTRUCTION/O0` | 9956484 | 11008722 |
| `point_cloud_summary` | full | S3 `PER_INSTRUCTION/O1` | 9170726 | 9258195 |
| `point_cloud_summary` | full | S3 `PURE_EXPERIMENTAL/O0` | 9643428 | 10953637 |
| `point_cloud_summary` | full | S3 `PURE_EXPERIMENTAL/O1` | 9204165 | 9377642 |
| `point_cloud_summary` | full | Zig `Debug/Debug` | 8755007 | 8993579 |
| `point_cloud_summary` | full | Zig `ReleaseFast/ReleaseFast` | 8569285 | 11886813 |
| `point_cloud_summary` | medium | Clang `O0/O0` | 7517722 | 7763213 |
| `point_cloud_summary` | medium | Clang `O2/O2` | 7758273 | 8212580 |
| `point_cloud_summary` | medium | GCC `O0/O0` | 6165014 | 6675851 |
| `point_cloud_summary` | medium | GCC `O2/O2` | 6362620 | 8101623 |
| `point_cloud_summary` | medium | Python `CPython/interpreted` | 91860636 | 98000459 |
| `point_cloud_summary` | medium | Rust `opt-level-0/opt-level-0` | 8122172 | 8863076 |
| `point_cloud_summary` | medium | Rust `opt-level-2/opt-level-2` | 6884172 | 7063129 |
| `point_cloud_summary` | medium | S3 `EXACT_SEGMENT/O0` | 9389582 | 10417097 |
| `point_cloud_summary` | medium | S3 `EXACT_SEGMENT/O1` | 8661404 | 11170845 |
| `point_cloud_summary` | medium | S3 `LOOP_HYBRID/O0` | 11467334 | 11777630 |
| `point_cloud_summary` | medium | S3 `LOOP_HYBRID/O1` | 10278169 | 10769136 |
| `point_cloud_summary` | medium | S3 `PER_INSTRUCTION/O0` | 9695247 | 10149735 |
| `point_cloud_summary` | medium | S3 `PER_INSTRUCTION/O1` | 9830925 | 10834096 |
| `point_cloud_summary` | medium | S3 `PURE_EXPERIMENTAL/O0` | 11402270 | 12299386 |
| `point_cloud_summary` | medium | S3 `PURE_EXPERIMENTAL/O1` | 9377858 | 10963727 |
| `point_cloud_summary` | medium | Zig `Debug/Debug` | 7194377 | 9862120 |
| `point_cloud_summary` | medium | Zig `ReleaseFast/ReleaseFast` | 5618312 | 5837138 |
| `point_cloud_summary` | small | Clang `O0/O0` | 8261410 | 8552886 |
| `point_cloud_summary` | small | Clang `O2/O2` | 7419123 | 7602224 |
| `point_cloud_summary` | small | GCC `O0/O0` | 8671144 | 11098805 |
| `point_cloud_summary` | small | GCC `O2/O2` | 7066734 | 7405318 |
| `point_cloud_summary` | small | Python `CPython/interpreted` | 81175443 | 93659828 |
| `point_cloud_summary` | small | Rust `opt-level-0/opt-level-0` | 7465782 | 7906882 |
| `point_cloud_summary` | small | Rust `opt-level-2/opt-level-2` | 6768294 | 7603635 |
| `point_cloud_summary` | small | S3 `EXACT_SEGMENT/O0` | 10275284 | 12340466 |
| `point_cloud_summary` | small | S3 `EXACT_SEGMENT/O1` | 9042514 | 9084387 |
| `point_cloud_summary` | small | S3 `LOOP_HYBRID/O0` | 9796286 | 16714073 |
| `point_cloud_summary` | small | S3 `LOOP_HYBRID/O1` | 9431872 | 9452587 |
| `point_cloud_summary` | small | S3 `PER_INSTRUCTION/O0` | 10335207 | 10349562 |
| `point_cloud_summary` | small | S3 `PER_INSTRUCTION/O1` | 10628673 | 11173515 |
| `point_cloud_summary` | small | S3 `PURE_EXPERIMENTAL/O0` | 10861829 | 10872214 |
| `point_cloud_summary` | small | S3 `PURE_EXPERIMENTAL/O1` | 9478201 | 10176360 |
| `point_cloud_summary` | small | Zig `Debug/Debug` | 8116602 | 8451697 |
| `point_cloud_summary` | small | Zig `ReleaseFast/ReleaseFast` | 9222011 | 10737141 |

## Cost of the S3 control mechanism

Paired ratio is `controlled / pure` for the same workload, size, round, compiler commit and optimization. Values above 1 mean slower than Pure; 1.00× is parity.

| Workload | Input | Controlled mode | Median paired ratio | 95% bootstrap CI |
|---|---:|---|---:|---:|
| `agent_energy_residual` | full | `EXACT_SEGMENT` | 1.188× | [0.963, 1.442]× |
| `agent_energy_residual` | full | `LOOP_HYBRID` | 1.358× | [0.929, 1.575]× |
| `agent_energy_residual` | full | `PER_INSTRUCTION` | 1.162× | [0.853, 1.441]× |
| `agent_energy_residual` | medium | `EXACT_SEGMENT` | 0.942× | [0.662, 1.186]× |
| `agent_energy_residual` | medium | `LOOP_HYBRID` | 0.927× | [0.676, 1.055]× |
| `agent_energy_residual` | medium | `PER_INSTRUCTION` | 0.974× | [0.855, 1.110]× |
| `agent_energy_residual` | small | `EXACT_SEGMENT` | 1.117× | [1.052, 1.475]× |
| `agent_energy_residual` | small | `LOOP_HYBRID` | 1.020× | [0.902, 1.252]× |
| `agent_energy_residual` | small | `PER_INSTRUCTION` | 1.004× | [0.779, 1.089]× |
| `agent_point_bounds` | full | `EXACT_SEGMENT` | 1.095× | [0.981, 1.337]× |
| `agent_point_bounds` | full | `LOOP_HYBRID` | 1.320× | [1.077, 1.647]× |
| `agent_point_bounds` | full | `PER_INSTRUCTION` | 1.004× | [0.930, 1.245]× |
| `agent_point_bounds` | medium | `EXACT_SEGMENT` | 1.130× | [1.022, 1.744]× |
| `agent_point_bounds` | medium | `LOOP_HYBRID` | 0.941× | [0.692, 1.021]× |
| `agent_point_bounds` | medium | `PER_INSTRUCTION` | 1.108× | [0.924, 1.696]× |
| `agent_point_bounds` | small | `EXACT_SEGMENT` | 0.887× | [0.815, 1.277]× |
| `agent_point_bounds` | small | `LOOP_HYBRID` | 1.239× | [0.956, 1.634]× |
| `agent_point_bounds` | small | `PER_INSTRUCTION` | 1.235× | [0.550, 1.332]× |
| `agent_raster_threshold_count` | full | `EXACT_SEGMENT` | 1.258× | [1.005, 1.771]× |
| `agent_raster_threshold_count` | full | `LOOP_HYBRID` | 1.247× | [0.867, 1.692]× |
| `agent_raster_threshold_count` | full | `PER_INSTRUCTION` | 1.052× | [0.962, 1.306]× |
| `agent_raster_threshold_count` | medium | `EXACT_SEGMENT` | 1.383× | [1.009, 1.596]× |
| `agent_raster_threshold_count` | medium | `LOOP_HYBRID` | 1.294× | [1.005, 1.885]× |
| `agent_raster_threshold_count` | medium | `PER_INSTRUCTION` | 1.131× | [0.973, 1.413]× |
| `agent_raster_threshold_count` | small | `EXACT_SEGMENT` | 1.131× | [1.007, 1.257]× |
| `agent_raster_threshold_count` | small | `LOOP_HYBRID` | 1.214× | [0.986, 1.627]× |
| `agent_raster_threshold_count` | small | `PER_INSTRUCTION` | 1.124× | [0.867, 1.329]× |
| `agent_raster_valid_mean` | full | `EXACT_SEGMENT` | 0.986× | [0.858, 1.490]× |
| `agent_raster_valid_mean` | full | `LOOP_HYBRID` | 1.165× | [0.898, 1.828]× |
| `agent_raster_valid_mean` | full | `PER_INSTRUCTION` | 0.904× | [0.792, 1.231]× |
| `agent_raster_valid_mean` | medium | `EXACT_SEGMENT` | 0.950× | [0.640, 1.099]× |
| `agent_raster_valid_mean` | medium | `LOOP_HYBRID` | 1.034× | [0.819, 1.164]× |
| `agent_raster_valid_mean` | medium | `PER_INSTRUCTION` | 0.861× | [0.611, 1.093]× |
| `agent_raster_valid_mean` | small | `EXACT_SEGMENT` | 0.977× | [0.859, 1.179]× |
| `agent_raster_valid_mean` | small | `LOOP_HYBRID` | 1.150× | [1.011, 1.236]× |
| `agent_raster_valid_mean` | small | `PER_INSTRUCTION` | 1.035× | [0.845, 1.168]× |
| `energy_series_aggregation` | full | `EXACT_SEGMENT` | 1.024× | [0.807, 1.319]× |
| `energy_series_aggregation` | full | `LOOP_HYBRID` | 1.107× | [0.998, 1.165]× |
| `energy_series_aggregation` | full | `PER_INSTRUCTION` | 1.092× | [1.020, 1.262]× |
| `energy_series_aggregation` | medium | `EXACT_SEGMENT` | 0.899× | [0.787, 1.151]× |
| `energy_series_aggregation` | medium | `LOOP_HYBRID` | 0.917× | [0.700, 1.098]× |
| `energy_series_aggregation` | medium | `PER_INSTRUCTION` | 0.910× | [0.754, 1.050]× |
| `energy_series_aggregation` | small | `EXACT_SEGMENT` | 1.464× | [1.033, 1.548]× |
| `energy_series_aggregation` | small | `LOOP_HYBRID` | 1.243× | [0.960, 1.451]× |
| `energy_series_aggregation` | small | `PER_INSTRUCTION` | 1.199× | [0.863, 1.430]× |
| `point_cloud_summary` | full | `EXACT_SEGMENT` | 1.082× | [0.974, 1.920]× |
| `point_cloud_summary` | full | `LOOP_HYBRID` | 1.116× | [1.003, 1.742]× |
| `point_cloud_summary` | full | `PER_INSTRUCTION` | 1.158× | [1.112, 1.634]× |
| `point_cloud_summary` | medium | `EXACT_SEGMENT` | 0.955× | [0.719, 1.310]× |
| `point_cloud_summary` | medium | `LOOP_HYBRID` | 0.974× | [0.591, 1.158]× |
| `point_cloud_summary` | medium | `PER_INSTRUCTION` | 1.025× | [0.796, 1.206]× |
| `point_cloud_summary` | small | `EXACT_SEGMENT` | 1.056× | [0.687, 1.191]× |
| `point_cloud_summary` | small | `LOOP_HYBRID` | 1.073× | [0.805, 1.167]× |
| `point_cloud_summary` | small | `PER_INSTRUCTION` | 1.119× | [1.012, 1.229]× |

## S3 Pure vs other implementations

Paired ratio is `S3 Pure O1 / other implementation` within each shuffled sample round. Python remains an interpreted comparison and is not included in any native ranking.

| Workload | Input | Comparator | Median ratio | 95% bootstrap CI |
|---|---:|---|---:|---:|
| `agent_energy_residual` | full | Clang `O2` | 30.750× | [23.143, 40.271]× |
| `agent_energy_residual` | full | GCC `O2` | 28.380× | [26.085, 33.929]× |
| `agent_energy_residual` | full | Python `CPython` | 0.519× | [0.302, 0.580]× |
| `agent_energy_residual` | full | Rust `opt-level-2` | 36.575× | [28.174, 38.619]× |
| `agent_energy_residual` | full | Zig `ReleaseFast` | 44.037× | [30.390, 49.529]× |
| `agent_energy_residual` | medium | Clang `O2` | 33.462× | [27.529, 42.904]× |
| `agent_energy_residual` | medium | GCC `O2` | 28.512× | [22.144, 31.840]× |
| `agent_energy_residual` | medium | Python `CPython` | 0.611× | [0.350, 0.708]× |
| `agent_energy_residual` | medium | Rust `opt-level-2` | 34.545× | [25.880, 43.775]× |
| `agent_energy_residual` | medium | Zig `ReleaseFast` | 41.159× | [32.365, 50.705]× |
| `agent_energy_residual` | small | Clang `O2` | 35.645× | [33.208, 40.281]× |
| `agent_energy_residual` | small | GCC `O2` | 33.450× | [31.103, 36.943]× |
| `agent_energy_residual` | small | Python `CPython` | 0.576× | [0.452, 0.732]× |
| `agent_energy_residual` | small | Rust `opt-level-2` | 35.785× | [24.431, 42.565]× |
| `agent_energy_residual` | small | Zig `ReleaseFast` | 37.818× | [27.838, 46.600]× |
| `agent_point_bounds` | full | Clang `O2` | 34.278× | [27.070, 42.400]× |
| `agent_point_bounds` | full | GCC `O2` | 30.098× | [27.745, 43.237]× |
| `agent_point_bounds` | full | Python `CPython` | 0.540× | [0.403, 0.619]× |
| `agent_point_bounds` | full | Rust `opt-level-2` | 26.255× | [15.824, 36.511]× |
| `agent_point_bounds` | full | Zig `ReleaseFast` | 24.873× | [21.559, 26.548]× |
| `agent_point_bounds` | medium | Clang `O2` | 41.250× | [37.020, 48.553]× |
| `agent_point_bounds` | medium | GCC `O2` | 33.787× | [28.710, 38.562]× |
| `agent_point_bounds` | medium | Python `CPython` | 0.503× | [0.418, 0.546]× |
| `agent_point_bounds` | medium | Rust `opt-level-2` | 31.780× | [24.265, 48.872]× |
| `agent_point_bounds` | medium | Zig `ReleaseFast` | 29.132× | [21.447, 30.941]× |
| `agent_point_bounds` | small | Clang `O2` | 36.780× | [24.857, 45.440]× |
| `agent_point_bounds` | small | GCC `O2` | 30.106× | [27.446, 38.298]× |
| `agent_point_bounds` | small | Python `CPython` | 0.523× | [0.366, 0.646]× |
| `agent_point_bounds` | small | Rust `opt-level-2` | 28.734× | [24.333, 52.289]× |
| `agent_point_bounds` | small | Zig `ReleaseFast` | 26.087× | [23.053, 39.860]× |
| `agent_raster_threshold_count` | full | Clang `O2` | 10.100× | [7.600, 15.596]× |
| `agent_raster_threshold_count` | full | GCC `O2` | 16.833× | [15.222, 25.190]× |
| `agent_raster_threshold_count` | full | Python `CPython` | 0.375× | [0.351, 0.591]× |
| `agent_raster_threshold_count` | full | Rust `opt-level-2` | 11.479× | [8.798, 14.908]× |
| `agent_raster_threshold_count` | full | Zig `ReleaseFast` | 24.344× | [14.530, 28.333]× |
| `agent_raster_threshold_count` | medium | Clang `O2` | 8.066× | [6.624, 11.781]× |
| `agent_raster_threshold_count` | medium | GCC `O2` | 16.103× | [9.608, 21.611]× |
| `agent_raster_threshold_count` | medium | Python `CPython` | 0.529× | [0.368, 0.755]× |
| `agent_raster_threshold_count` | medium | Rust `opt-level-2` | 10.060× | [7.367, 12.250]× |
| `agent_raster_threshold_count` | medium | Zig `ReleaseFast` | 26.465× | [19.316, 32.333]× |
| `agent_raster_threshold_count` | small | Clang `O2` | 11.762× | [8.485, 14.865]× |
| `agent_raster_threshold_count` | small | GCC `O2` | 18.854× | [14.028, 22.403]× |
| `agent_raster_threshold_count` | small | Python `CPython` | 0.630× | [0.414, 1.088]× |
| `agent_raster_threshold_count` | small | Rust `opt-level-2` | 11.037× | [9.344, 15.000]× |
| `agent_raster_threshold_count` | small | Zig `ReleaseFast` | 27.091× | [19.114, 42.472]× |
| `agent_raster_valid_mean` | full | Clang `O2` | 23.204× | [18.553, 36.163]× |
| `agent_raster_valid_mean` | full | GCC `O2` | 23.051× | [17.489, 34.747]× |
| `agent_raster_valid_mean` | full | Python `CPython` | 0.579× | [0.418, 0.721]× |
| `agent_raster_valid_mean` | full | Rust `opt-level-2` | 27.071× | [20.296, 29.059]× |
| `agent_raster_valid_mean` | full | Zig `ReleaseFast` | 27.494× | [19.200, 31.139]× |
| `agent_raster_valid_mean` | medium | Clang `O2` | 26.686× | [22.852, 34.426]× |
| `agent_raster_valid_mean` | medium | GCC `O2` | 30.239× | [16.386, 35.281]× |
| `agent_raster_valid_mean` | medium | Python `CPython` | 0.757× | [0.539, 1.107]× |
| `agent_raster_valid_mean` | medium | Rust `opt-level-2` | 27.013× | [22.551, 31.635]× |
| `agent_raster_valid_mean` | medium | Zig `ReleaseFast` | 25.087× | [21.889, 28.278]× |
| `agent_raster_valid_mean` | small | Clang `O2` | 33.431× | [23.420, 36.923]× |
| `agent_raster_valid_mean` | small | GCC `O2` | 26.492× | [20.221, 31.203]× |
| `agent_raster_valid_mean` | small | Python `CPython` | 0.629× | [0.417, 0.924]× |
| `agent_raster_valid_mean` | small | Rust `opt-level-2` | 24.857× | [20.893, 33.903]× |
| `agent_raster_valid_mean` | small | Zig `ReleaseFast` | 24.168× | [20.038, 27.532]× |
| `energy_series_aggregation` | full | Clang `O2` | 41.585× | [39.101, 51.084]× |
| `energy_series_aggregation` | full | GCC `O2` | 43.393× | [38.974, 49.745]× |
| `energy_series_aggregation` | full | Python `CPython` | 0.502× | [0.460, 0.642]× |
| `energy_series_aggregation` | full | Rust `opt-level-2` | 41.897× | [33.890, 53.806]× |
| `energy_series_aggregation` | full | Zig `ReleaseFast` | 52.075× | [44.696, 62.676]× |
| `energy_series_aggregation` | medium | Clang `O2` | 40.698× | [35.052, 43.719]× |
| `energy_series_aggregation` | medium | GCC `O2` | 36.514× | [29.987, 42.915]× |
| `energy_series_aggregation` | medium | Python `CPython` | 0.587× | [0.509, 0.724]× |
| `energy_series_aggregation` | medium | Rust `opt-level-2` | 41.220× | [30.413, 46.654]× |
| `energy_series_aggregation` | medium | Zig `ReleaseFast` | 53.986× | [40.427, 61.868]× |
| `energy_series_aggregation` | small | Clang `O2` | 34.448× | [34.237, 46.639]× |
| `energy_series_aggregation` | small | GCC `O2` | 38.442× | [30.439, 45.486]× |
| `energy_series_aggregation` | small | Python `CPython` | 0.473× | [0.423, 0.573]× |
| `energy_series_aggregation` | small | Rust `opt-level-2` | 35.304× | [28.163, 44.012]× |
| `energy_series_aggregation` | small | Zig `ReleaseFast` | 36.697× | [29.463, 43.232]× |
| `point_cloud_summary` | full | Clang `O2` | 46.188× | [33.522, 56.800]× |
| `point_cloud_summary` | full | GCC `O2` | 42.859× | [29.631, 51.133]× |
| `point_cloud_summary` | full | Python `CPython` | 0.412× | [0.274, 0.537]× |
| `point_cloud_summary` | full | Rust `opt-level-2` | 37.415× | [33.194, 45.663]× |
| `point_cloud_summary` | full | Zig `ReleaseFast` | 30.767× | [23.756, 41.934]× |
| `point_cloud_summary` | medium | Clang `O2` | 49.262× | [40.704, 63.905]× |
| `point_cloud_summary` | medium | GCC `O2` | 43.349× | [33.218, 52.595]× |
| `point_cloud_summary` | medium | Python `CPython` | 0.355× | [0.262, 0.416]× |
| `point_cloud_summary` | medium | Rust `opt-level-2` | 43.098× | [36.135, 50.898]× |
| `point_cloud_summary` | medium | Zig `ReleaseFast` | 35.846× | [33.843, 50.138]× |
| `point_cloud_summary` | small | Clang `O2` | 47.655× | [38.949, 58.179]× |
| `point_cloud_summary` | small | GCC `O2` | 39.865× | [23.562, 47.000]× |
| `point_cloud_summary` | small | Python `CPython` | 0.358× | [0.343, 0.390]× |
| `point_cloud_summary` | small | Rust `opt-level-2` | 39.421× | [37.018, 43.460]× |
| `point_cloud_summary` | small | Zig `ReleaseFast` | 41.042× | [34.387, 46.278]× |

## Build time, ELF size, and static S3 code shape

Compile and link are separate wall-clock observations. S3 compile time includes frontend/optimizer, backend assembly generation and assembler; link time is separate. Rust code-generation time is the rustc total minus the measured linker proxy wall time. Static instruction counts are disassembly counts, not dynamic instruction counts.

| Artifact | Profile | Compile s | Link s | ELF bytes | `.text` bytes | Static insns* | SHA-256 |
|---|---|---:|---:|---:|---:|---:|---|
| `clang-o0` | O0 | 0.123583831 | 0.148640361 | 15592 | 3195 | n/a | `22060b4e57f6fad7fa0aef6669277b6ebaedb3b3d166931b7865ef2d59b5b4fb` |
| `clang-o2` | O2 | 0.214776468 | 0.111179806 | 15592 | 1751 | n/a | `cc7fd777367ffddd781235d649a67a8fa25f3a9e59061ee98baf1b21ce89a517` |
| `gcc-o0` | O0 | 0.093909569 | 0.040327279 | 15696 | 3354 | n/a | `eb760b7985af58a491977eb79af754e2f897e6c536a1af0d96fb82ff34bf3349` |
| `gcc-o2` | O2 | 0.31310643 | 0.054165643 | 15696 | 1962 | n/a | `a63f66f2d417c0ed5f3e27ca8899275d3c417b42628228804ff6ab86bb13374d` |
| `rust-optlevel0` | opt-level-0 | 0.33564796 | 0.386862793 | 11765072 | 257386 | n/a | `5ef8e90d3fcdc52801c62c94279085bc5a4d7c057c6d780f6849045ef345f01e` |
| `rust-optlevel2` | opt-level-2 | 0.436829023 | 0.326849303 | 11331384 | 1911 | n/a | `484ac6f02dc7ff71889447e7d75abfc934f73611497206d34923e02ab0a45685` |
| `s3-exact_segment-o0-agent_energy_residual` | EXACT_SEGMENT/O0 | 0.45124823599999997 | 0.019624516 | 225680 | 68801 | 12089 | `7f498c37375d4bfa6186d0e2a21cd105b27c33b7c1e7a3e3ffb1773462d4e9f2` |
| `s3-exact_segment-o0-agent_point_bounds` | EXACT_SEGMENT/O0 | 0.671359158 | 0.040090616 | 254344 | 77546 | 13627 | `a393bbaf29295d3af0a4d5f47d8407066433249da21f5a9ce1013c85b22d5eb7` |
| `s3-exact_segment-o0-agent_raster_threshold_count` | EXACT_SEGMENT/O0 | 0.617308708 | 0.994118117 | 197016 | 57404 | 10192 | `08a11d79dbb7ce3f7b08a7783e60d0b902725683d780fe270ede4c08df175f42` |
| `s3-exact_segment-o0-agent_raster_valid_mean` | EXACT_SEGMENT/O0 | 0.551474797 | 0.512429064 | 217488 | 66243 | 11648 | `700686931f1318f28eb76598b60c939d7d9bba7479b5b626d4e19e9027e86986` |
| `s3-exact_segment-o0-energy_series_aggregation` | EXACT_SEGMENT/O0 | 0.387571765 | 0.12515102 | 172744 | 52423 | 9475 | `13c97add7dca540db3cc4f763afd2610e46cfbfb56141ce3d73161fa8a5b3d38` |
| `s3-exact_segment-o0-point_cloud_summary` | EXACT_SEGMENT/O0 | 0.8886696249999999 | 0.239076189 | 278920 | 85232 | 14951 | `82529e81e19f78d4977d66de6d2e0ad5af8f4f0277c2b1ec6d613f0970b93ab9` |
| `s3-exact_segment-o1-agent_energy_residual` | EXACT_SEGMENT/O1 | 0.628925325 | 0.022056979 | 225680 | 68715 | 12075 | `e2c25aa97d85a3061356a7c9b33b80d702e9e15a76425562c527c8b206b3acd4` |
| `s3-exact_segment-o1-agent_point_bounds` | EXACT_SEGMENT/O1 | 1.393941044 | 0.02914157 | 254344 | 77460 | 13613 | `55469453be09429b83a05277410ac525638623735e21114ec37f6b7683b25373` |
| `s3-exact_segment-o1-agent_raster_threshold_count` | EXACT_SEGMENT/O1 | 1.3807942219999998 | 0.055855227 | 192920 | 57275 | 10171 | `2d0a0cfdf884a61ccf65a3155d5d823cc012fb2e696d92427f1fb1b33945b8b2` |
| `s3-exact_segment-o1-agent_raster_valid_mean` | EXACT_SEGMENT/O1 | 0.979674701 | 0.069887923 | 217488 | 66157 | 11634 | `eb10e9637e6f5d48522402ce10d756b60fcef17ea5313fe2850469945d971c8a` |
| `s3-exact_segment-o1-energy_series_aggregation` | EXACT_SEGMENT/O1 | 0.965814799 | 0.108819098 | 172744 | 52423 | 9475 | `447a7d3c7be3f850931cdad783576d2e1475e7cdfdfa9dbbb8daf505e61983cd` |
| `s3-exact_segment-o1-point_cloud_summary` | EXACT_SEGMENT/O1 | 0.67709493 | 0.030620466 | 278920 | 85232 | 14951 | `758f5199f75c3ed2a892c85d6ac4ce8db7fe8ec1ddceedffdd95fe4594cfe535` |
| `s3-loop_hybrid-o0-agent_energy_residual` | LOOP_HYBRID/O0 | 0.528818068 | 0.037198441 | 217480 | 57739 | 10259 | `4407abd3bae3e1642e32990109eec0faf336e54c5a60d810180c53fed5ee857a` |
| `s3-loop_hybrid-o0-agent_point_bounds` | LOOP_HYBRID/O0 | 0.521909419 | 0.115296156 | 246152 | 66693 | 11814 | `daff6a34151c0c7b6d0a3a7c93be9969ca6f93d7f5656ad034f00a8d362b7555` |
| `s3-loop_hybrid-o0-agent_raster_threshold_count` | LOOP_HYBRID/O0 | 0.638483941 | 0.147080342 | 184728 | 47167 | 8503 | `95cdf29dee8854dbbc733d8a5d3bb608b90de712a16a8d510131dbb45c20cc7e` |
| `s3-loop_hybrid-o0-agent_raster_valid_mean` | LOOP_HYBRID/O0 | 0.596245351 | 0.133180775 | 205200 | 54729 | 9744 | `dab018de7b1ea4e783a32755ae27c5f2cf5629983ea408bcb84830936b2537db` |
| `s3-loop_hybrid-o0-energy_series_aggregation` | LOOP_HYBRID/O0 | 0.42334181400000004 | 0.091722448 | 168640 | 45602 | 8314 | `dadeff6cd603da6cf43350ee4040ead9d6f3cfd423411a8fb1d0d769f75cdef8` |
| `s3-loop_hybrid-o0-point_cloud_summary` | LOOP_HYBRID/O0 | 0.570284732 | 0.024626454 | 270728 | 76771 | 13514 | `6d83fb6706ab5b45c815e39b0aeaa3ad89fd9943c07f260d2a5764eb334ca68a` |
| `s3-loop_hybrid-o1-agent_energy_residual` | LOOP_HYBRID/O1 | 0.513564755 | 0.034507671 | 217480 | 57653 | 10245 | `d69c14d4259ce1f32d44309a9e917ff58b49bd215165419aac03cdd02bd24090` |
| `s3-loop_hybrid-o1-agent_point_bounds` | LOOP_HYBRID/O1 | 1.397417982 | 0.158093207 | 246152 | 66607 | 11800 | `b6111792204b6060a7be523303a103bddab342186dfa25471c65b9e9a909a923` |
| `s3-loop_hybrid-o1-agent_raster_threshold_count` | LOOP_HYBRID/O1 | 0.7482311150000001 | 0.13841947 | 184728 | 47038 | 8482 | `370423ca5fc0c04065af398263bd59a631acb141342c2ed9680609c273aec148` |
| `s3-loop_hybrid-o1-agent_raster_valid_mean` | LOOP_HYBRID/O1 | 4.540431879 | 0.556546997 | 205200 | 54643 | 9730 | `5e2182f154d38cafd6dfc4668e81c14d71369d0e90351a17c8ce2c78413c7ee0` |
| `s3-loop_hybrid-o1-energy_series_aggregation` | LOOP_HYBRID/O1 | 0.26570095800000004 | 0.065693793 | 168640 | 45602 | 8314 | `8029e014cab3a8340081feb229d80b53ca21107fd8291efe302fb3be8ee76c64` |
| `s3-loop_hybrid-o1-point_cloud_summary` | LOOP_HYBRID/O1 | 0.7260826739999999 | 0.225909624 | 270728 | 76771 | 13514 | `25244964047130e2c0070728715bf105121cd0d7a477ba07d5cbfb34513feaa0` |
| `s3-per_instruction-o0-agent_energy_residual` | PER_INSTRUCTION/O0 | 2.895027734 | 0.036469805 | 209424 | 46675 | 9091 | `a913818a777047b3a04db5937a680ab65f52d016755cf1b6db11b967ac7e3a14` |
| `s3-per_instruction-o0-agent_point_bounds` | PER_INSTRUCTION/O0 | 0.523710237 | 0.069248488 | 233992 | 52544 | 10165 | `491bcdf26cd10294efd2817022c6fb4a9d1af560309a9a8acc56eb0dfc08e887` |
| `s3-per_instruction-o0-agent_raster_threshold_count` | PER_INSTRUCTION/O0 | 0.510319537 | 0.172201597 | 180768 | 39153 | 7741 | `cd0c714679c81fdeeabcf812be8be101b0a60978c936acc5ca05216a512eb91c` |
| `s3-per_instruction-o0-agent_raster_valid_mean` | PER_INSTRUCTION/O0 | 0.710672937 | 0.308911261 | 201232 | 44921 | 8779 | `7a58eb413f9c37872f43def2aab9b88e2c1ae20fb353c0c91dbd5b079f512176` |
| `s3-per_instruction-o0-energy_series_aggregation` | PER_INSTRUCTION/O0 | 0.467396627 | 0.983614725 | 160584 | 36255 | 7231 | `7e39ea2f870431da12205a7ccd066b1f7ad6403a282d1a285867c826b0f4b7cb` |
| `s3-per_instruction-o0-point_cloud_summary` | PER_INSTRUCTION/O0 | 0.525638222 | 0.06096326 | 258568 | 58063 | 11137 | `31a2ac73fafb3c048b689ba4301d94acc4f2852c11883d707846018f5b676675` |
| `s3-per_instruction-o1-agent_energy_residual` | PER_INSTRUCTION/O1 | 7.151812709 | 0.51490295 | 209424 | 46619 | 9079 | `4dc9f2187dcbb116454d4435f75610392fae47bfc57066abc5ec614b4078cdd2` |
| `s3-per_instruction-o1-agent_point_bounds` | PER_INSTRUCTION/O1 | 0.758127284 | 0.098056531 | 233992 | 52488 | 10153 | `495dd6dee286fa3e79e2f0ebd42d80b70146b2d4e4896f056d660b1340f7abc9` |
| `s3-per_instruction-o1-agent_raster_threshold_count` | PER_INSTRUCTION/O1 | 0.542151297 | 0.078905668 | 180768 | 39069 | 7723 | `71d9731adf5932953d9b83292edd2e4d6ca5c8bfde991a6608893fe1dd3f96fb` |
| `s3-per_instruction-o1-agent_raster_valid_mean` | PER_INSTRUCTION/O1 | 0.48480346700000004 | 0.896228685 | 201232 | 44865 | 8767 | `9b22f02b9b19fd32f6ca1bb0292258b6d6326453ab9a39b3b571ed9f1c38ab07` |
| `s3-per_instruction-o1-energy_series_aggregation` | PER_INSTRUCTION/O1 | 0.401028016 | 0.659478937 | 160584 | 36255 | 7231 | `b822337beee3950434cfea9634117119368cfcaada8250839e487e198f9da47f` |
| `s3-per_instruction-o1-point_cloud_summary` | PER_INSTRUCTION/O1 | 0.403925409 | 0.176624012 | 258568 | 58063 | 11137 | `da49f35e0fb332db1ab51e54a63d3aed799fa5a9b7879efbd135ab97152f2147` |
| `s3-pure_experimental-o0-agent_energy_residual` | PURE_EXPERIMENTAL/O0 | 0.441420926 | 0.106817129 | 127376 | 34723 | 6809 | `ad6dbc03835e62e5e46c49dc34c87a6d0f2ce65373a11b265a4c153b3f2625c3` |
| `s3-pure_experimental-o0-agent_point_bounds` | PURE_EXPERIMENTAL/O0 | 0.481901492 | 0.143690085 | 147848 | 39561 | 7683 | `377d01c03ded05eee80fa6b60ecb46bd8bb672c41d666329fb50afc00300db22` |
| `s3-pure_experimental-o0-agent_raster_threshold_count` | PURE_EXPERIMENTAL/O0 | 0.355805056 | 0.370285138 | 111008 | 29125 | 5829 | `37d1754e49c3d504e7fd7152003521a69b3f395434677a091a2416b0a4a2445e` |
| `s3-pure_experimental-o0-agent_raster_valid_mean` | PURE_EXPERIMENTAL/O0 | 1.064177562 | 0.078834275 | 123288 | 33166 | 6538 | `cdd7ee102e7d3e98d00f12e3eaa228da81b5d93ae1a46fec103830cc6be2bb58` |
| `s3-pure_experimental-o0-energy_series_aggregation` | PURE_EXPERIMENTAL/O0 | 6.138304087999999 | 0.089509613 | 103112 | 27791 | 5615 | `6d5d595590800d394e8fea527190d889dbd08916ef629d8e7b80e679579bacc2` |
| `s3-pure_experimental-o0-point_cloud_summary` | PURE_EXPERIMENTAL/O0 | 0.6590413310000001 | 0.104883518 | 164240 | 44404 | 8522 | `5be14170db7f11ac790ccc1a58897244c7ecfd64c6a3f843dce03ec211695072` |
| `s3-pure_experimental-o1-agent_energy_residual` | PURE_EXPERIMENTAL/O1 | 0.458631454 | 0.174600391 | 127376 | 34719 | 6807 | `fd3f01be4e1e96950fb6d2d7171197091e9e86633b9a9cd28afcffa37b22cc9d` |
| `s3-pure_experimental-o1-agent_point_bounds` | PURE_EXPERIMENTAL/O1 | 1.2543588380000001 | 0.217206255 | 147848 | 39557 | 7681 | `d6fa3baa69196a2eb6a700047c710534e6660414e4e06bc8ef19b07e7764f998` |
| `s3-pure_experimental-o1-agent_raster_threshold_count` | PURE_EXPERIMENTAL/O1 | 0.941039698 | 0.269964758 | 111008 | 29119 | 5826 | `d25c239d295d3fa049889e3fb1ff185b9afac88e1993938ca6fc1c32424f91ef` |
| `s3-pure_experimental-o1-agent_raster_valid_mean` | PURE_EXPERIMENTAL/O1 | 1.368457669 | 0.779042706 | 123288 | 33162 | 6536 | `6c74f1129827a068517832077565dfb8f9f24f2ee295513085fec6afb5f0e639` |
| `s3-pure_experimental-o1-energy_series_aggregation` | PURE_EXPERIMENTAL/O1 | 1.523471953 | 0.261672491 | 103112 | 27791 | 5615 | `6d6809881d8cfc9df73a72d7ce17217fcc4042559c9432937f38610df9cd7d7b` |
| `s3-pure_experimental-o1-point_cloud_summary` | PURE_EXPERIMENTAL/O1 | 0.679769403 | 0.058685823 | 164240 | 44404 | 8522 | `29d267371b208d4bb42c19d490369cf764ace5f8f8ac0fe7f2cccf3e5e9356eb` |
| `zig-debug` | Debug | 8.920095451 | 54.224953015 | 2564432 | 694826 | n/a | `4300b8997e290037a9a8f1c14e013d2accc3480fbf16568eb4a53e13ccee0f1b` |
| `zig-releasefast` | ReleaseFast | 0.655129355 | 0.176001253 | 12792 | 1530 | n/a | `217d52bc813392aced95174e05f3b1b8acc94e6f41e36c1ffe08b347a57e0611` |

Observed maximum control ratio: `energy_series_aggregation|small|EXACT_SEGMENT` at **1.464×** (paired 95% bootstrap CI [1.033, 1.548]×). This is a corpus observation, not a universal overhead claim.
Largest observed Pure/native residual: `energy_series_aggregation|medium|Zig|ReleaseFast` at **53.986×**. This identifies a follow-up candidate, not its cause.
Largest O1 PER_INSTRUCTION minus Pure `.text` delta: `point_cloud_summary`, **+13659 bytes** (static section size only).
Calibration note: high-repetition controlled O0 `point_cloud_summary` exhausted the existing 100,000 logical-instruction budget when many calls accumulated in one process. The final protocol uses a base of one call (8/2/1 calls for small/medium/full per process), preserving the cap and approximately normalizing input work; this failed calibration is not a performance result.

## Interpretation and limits

- The paired control-cost ratios are measured at all three input sizes, over six workloads, and use the same pinned compiler commit and optimization level within each S3 pair.
- Runtime-cell CV reached 3.431; the 15-sample, short-batch results are descriptive. Ratios whose paired confidence intervals include 1.00× do not resolve a difference in this run.
- Process peak RSS includes the process and loader baseline, not just the kernel. Identical RSS medians are nondiscriminating and do not support a claim of equal kernel memory use.
- `.text` size and static disassembly explain generated-code growth only. They do not prove dynamic instruction counts, CPU bottlenecks, vectorization behavior, or causality.
- FFI dispatch is included equally through one C harness and is intentionally not subtracted. `process_initialization_wall_ns` includes process spawn, dynamic loader/interpreter, fixture loading and a correctness call; it is not a pure OS process-creation metric.
- S3 Pure removes only dynamic instruction-budget accounting. Untimed invalid-output probes require status 2 across all S3 profiles; valid data parity is required for every measured sample.
- No parser workload was accepted in this pinned V6-native subset, so parsing is explicitly unavailable rather than replaced with a simplified algorithm.
- See `run-manifest.json`, `builds.jsonl`, `raw_samples.jsonl`, `startup_samples.jsonl`, `invalid_cases.jsonl`, `runtime-fixture-v1.bin`, and `expected-v1.json` for reproducible raw evidence.
