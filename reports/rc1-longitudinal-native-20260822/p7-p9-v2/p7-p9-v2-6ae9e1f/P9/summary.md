# P9 native workload

{
  "control_drift_percent": 77.30825432886644,
  "control_stable": false,
  "control_stats": {
    "count": 30,
    "iqr": 623.202392578125,
    "mad": 325.146484375,
    "max": 5748.2314453125,
    "mean": 4294.704427083333,
    "median": 4241.2294921875,
    "min": 3241.9423828125,
    "p25": 3948.841552734375,
    "p75": 4572.0439453125
  },
  "correctness": {
    "control_result": 44,
    "status": "PASS",
    "variants": {
      "C-O0": 44,
      "C-O2": 44,
      "C-O3": 44,
      "H4-O0": 44,
      "H4-O1": 44,
      "H5-O0": 44,
      "H5-O1": 44
    }
  },
  "inputs_pinned": true,
  "name": "arrays and memory",
  "oracle_defined": true,
  "paired": {
    "rc1_vs_c_o2_percent": [
      -26.216276478927945,
      -33.9474148723393,
      -16.677241927755894,
      -1.675862288068286,
      -22.290797614411552,
      8.430339066962755,
      -17.376403230785918,
      -15.413903818746089,
      -30.05289732480213,
      -9.980193022848304,
      -13.50587093343738,
      -23.23200644954101,
      -8.37912372444416,
      -14.009074098566431,
      -21.362109545597097,
      -8.130582234980722,
      17.007012463031113,
      -31.59926400421601,
      -20.842208251286465,
      29.175638396987758,
      -20.55203696470236,
      -29.230226049878528,
      -42.69170606514913,
      16.525733086156546,
      -23.18766420761579,
      -12.003991085276844,
      3.7673235142466455,
      -28.626200264529,
      -32.39533905940297,
      3.177427915898101
    ],
    "rc1_vs_m230_percent": [
      -10.655726203258231,
      5.058478260105925,
      -2.392483128874634,
      10.418828398390922,
      20.116620472553137,
      31.62017461995641,
      0.12057561199738664,
      8.597141810467267,
      3.147978915790417,
      2.042988264208301,
      -5.291097362422659,
      4.287166552170407,
      9.779052582890536,
      -6.267393923185571,
      -8.713293514366438,
      -7.969248616526725,
      21.854646345554585,
      -9.097286010704098,
      -21.023938296345356,
      27.991968244573062,
      -10.042934257551494,
      -0.9729158087270484,
      -13.911341137902866,
      20.87951511015891,
      -20.197093657895437,
      37.154544713658886,
      23.07255638937813,
      -9.858005399383284,
      -32.570204036362725,
      45.85951857737231
    ]
  },
  "perf": "DEFERRED_BY_ENVIRONMENT",
  "protocol": {
    "cpu_affinity": "taskset -c 0",
    "operations_per_run": 1024,
    "repetitions": 30,
    "schedule": "rotating C-O0 C-O2 C-O3 H4-O0 H4-O1 H5-O0 H5-O1",
    "timing": "native process execution excluding compilation",
    "warmups": 5
  },
  "provenance": {
    "benchmark_sha": "6ae9e1f8bcff79557c02eb20c786e70d42eeda1d",
    "s3_shas": {
      "H4": "e23b092bec100cedc520841a7dd0f4488090b6a1",
      "H5": "9b39c7070d7bfa23d709c2128eb0b0bbef164177"
    }
  },
  "raw_samples": "raw/samples.json",
  "repeatable": false,
  "run_id": "p7-p9-v2-6ae9e1f",
  "sample_level_data_available": "YES",
  "schema": "s3.rc1.p7-p9.native-summary.v1",
  "status": "EXPERIMENTAL",
  "structural": {
    "c": {
      "O0": {
        "binary_size_bytes": 16000,
        "branch_count": 6,
        "call_count": 2,
        "cond_branch_count": 4,
        "instruction_count": 61,
        "line_count": 103,
        "load_store_count": 0,
        "stack_ops_count": 0,
        "text_section_bytes": 1766,
        "variant": "C-P9-O0"
      },
      "O2": {
        "binary_size_bytes": 16008,
        "branch_count": 3,
        "call_count": 2,
        "cond_branch_count": 3,
        "instruction_count": 40,
        "line_count": 110,
        "load_store_count": 0,
        "stack_ops_count": 0,
        "text_section_bytes": 1805,
        "variant": "C-P9-O2"
      },
      "O3": {
        "binary_size_bytes": 15960,
        "branch_count": 1,
        "call_count": 1,
        "cond_branch_count": 1,
        "instruction_count": 90,
        "line_count": 128,
        "load_store_count": 0,
        "stack_ops_count": 0,
        "text_section_bytes": 1786,
        "variant": "C-P9-O3"
      }
    },
    "s3": {
      "H4": {
        "O0": {
          "binary_size_bytes": 61496,
          "branch_count": 738,
          "call_count": 36,
          "cond_branch_count": 385,
          "instruction_count": 3316,
          "line_count": 4576,
          "load_store_count": 1543,
          "stack_ops_count": 405,
          "text_section_bytes": 47496,
          "variant": "H4-P9-O0"
        },
        "O1": {
          "binary_size_bytes": 60664,
          "branch_count": 726,
          "call_count": 36,
          "cond_branch_count": 379,
          "instruction_count": 3270,
          "line_count": 4514,
          "load_store_count": 1521,
          "stack_ops_count": 475,
          "text_section_bytes": 46693,
          "variant": "H4-P9-O1"
        }
      },
      "H5": {
        "O0": {
          "binary_size_bytes": 61496,
          "branch_count": 738,
          "call_count": 36,
          "cond_branch_count": 385,
          "instruction_count": 3316,
          "line_count": 4576,
          "load_store_count": 1543,
          "stack_ops_count": 405,
          "text_section_bytes": 47496,
          "variant": "H5-P9-O0"
        },
        "O1": {
          "binary_size_bytes": 60664,
          "branch_count": 726,
          "call_count": 36,
          "cond_branch_count": 379,
          "instruction_count": 3270,
          "line_count": 4514,
          "load_store_count": 1521,
          "stack_ops_count": 475,
          "text_section_bytes": 46693,
          "variant": "H5-P9-O1"
        }
      }
    }
  },
  "summaries": [
    {
      "checkpoint": "C",
      "count": 30,
      "iqr": 674.224609375,
      "mad": 353.08544921875,
      "max": 5337.5439453125,
      "mean": 4344.443326822917,
      "median": 4308.28271484375,
      "min": 3285.8173828125,
      "p25": 4045.8359375,
      "p75": 4720.060546875,
      "variant": "O0"
    },
    {
      "checkpoint": "C",
      "count": 30,
      "iqr": 623.202392578125,
      "mad": 325.146484375,
      "max": 5748.2314453125,
      "mean": 4294.704427083333,
      "median": 4241.2294921875,
      "min": 3241.9423828125,
      "p25": 3948.841552734375,
      "p75": 4572.0439453125,
      "variant": "O2"
    },
    {
      "checkpoint": "C",
      "count": 30,
      "iqr": 608.642578125,
      "mad": 337.2265625,
      "max": 5805.974609375,
      "mean": 4325.40537109375,
      "median": 4193.07666015625,
      "min": 3351.681640625,
      "p25": 3973.29541015625,
      "p75": 4581.93798828125,
      "variant": "O3"
    },
    {
      "checkpoint": "H4",
      "count": 30,
      "iqr": 568.289794921875,
      "mad": 273.03271484375,
      "max": 4768.2509765625,
      "mean": 3551.3322591145834,
      "median": 3489.89990234375,
      "min": 2496.26953125,
      "p25": 3287.251220703125,
      "p75": 3855.541015625,
      "variant": "O0"
    },
    {
      "checkpoint": "H4",
      "count": 30,
      "iqr": 377.85791015625,
      "mad": 176.0,
      "max": 4825.08203125,
      "mean": 3531.2737955729167,
      "median": 3506.98681640625,
      "min": 2980.8310546875,
      "p25": 3286.367431640625,
      "p75": 3664.225341796875,
      "variant": "O1"
    },
    {
      "checkpoint": "H5",
      "count": 30,
      "iqr": 833.072998046875,
      "mad": 424.1708984375,
      "max": 4942.5986328125,
      "mean": 3760.84658203125,
      "median": 3764.1123046875,
      "min": 2518.515625,
      "p25": 3290.43408203125,
      "p75": 4123.507080078125,
      "variant": "O0"
    },
    {
      "checkpoint": "H5",
      "count": 30,
      "iqr": 783.259765625,
      "mad": 412.486328125,
      "max": 4788.8291015625,
      "mean": 3635.324609375,
      "median": 3582.20361328125,
      "min": 2566.25,
      "p25": 3172.004638671875,
      "p75": 3955.264404296875,
      "variant": "O1"
    }
  ],
  "workload": "P9"
}
