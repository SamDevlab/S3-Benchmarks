# P8 native workload

{
  "control_drift_percent": 640.6806524882693,
  "control_stable": false,
  "control_stats": {
    "count": 30,
    "iqr": 2065.580078125,
    "mad": 1194.6123046875,
    "max": 42067.55078125,
    "mean": 9481.959244791668,
    "median": 8288.69140625,
    "min": 5679.580078125,
    "p25": 7082.09716796875,
    "p75": 9147.67724609375
  },
  "correctness": {
    "control_result": 7560,
    "status": "PASS",
    "variants": {
      "C-O0": 7560,
      "C-O2": 7560,
      "C-O3": 7560,
      "H4-O0": 7560,
      "H4-O1": 7560,
      "H5-O0": 7560,
      "H5-O1": 7560
    }
  },
  "inputs_pinned": true,
  "name": "call stack and ABI",
  "oracle_defined": true,
  "paired": {
    "rc1_vs_c_o2_percent": [
      -20.690171009000935,
      -3.1983505115138477,
      -38.37789285870975,
      -15.935233678960392,
      -12.22544433527657,
      -83.53870583704985,
      -10.233649193647965,
      -20.452530564409056,
      -22.222271199083355,
      -37.25616193372823,
      -14.493030427472275,
      -31.38820144231125,
      -33.04923599378099,
      -13.43989789685357,
      -13.333788057383334,
      -35.86298249333435,
      -16.137592077763085,
      -6.184495785621524,
      -29.02593831608151,
      -14.307115190528686,
      1.6552289688228194,
      -33.49239298362294,
      -25.086278195575616,
      2.948783930159382,
      -10.231108222473262,
      -14.271978535054842,
      -24.8396894034279,
      -19.154904277295305,
      -25.67606842278318,
      -34.681029614373614
    ],
    "rc1_vs_m230_percent": [
      -13.799921808815663,
      -7.136675766269995,
      -0.30964493615377453,
      1.7408820222815535,
      3.4563216474670977,
      30.579457784024022,
      -1.851527393845065,
      -18.114865430038364,
      -5.091772082867552,
      13.147609074927914,
      15.712147079925277,
      -15.257641866488958,
      9.551716094579987,
      14.619161114038004,
      2.285713487087615,
      -23.924128456046045,
      4.582022643727579,
      18.226187493499978,
      10.153744781049156,
      -25.563455358296107,
      46.2840347950656,
      4.550848232043614,
      2.5847674775995477,
      21.382940850179132,
      -1.4340307709269973,
      5.304799527724757,
      3.8363213422334175,
      13.998364171371481,
      -3.4009074699389297,
      -18.67058160219106
    ]
  },
  "perf": "DEFERRED_BY_ENVIRONMENT",
  "protocol": {
    "cpu_affinity": "taskset -c 0",
    "operations_per_run": 512,
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
        "binary_size_bytes": 16048,
        "branch_count": 3,
        "call_count": 6,
        "cond_branch_count": 2,
        "instruction_count": 91,
        "line_count": 165,
        "load_store_count": 0,
        "stack_ops_count": 0,
        "text_section_bytes": 1752,
        "variant": "C-P8-O0"
      },
      "O2": {
        "binary_size_bytes": 15960,
        "branch_count": 1,
        "call_count": 1,
        "cond_branch_count": 1,
        "instruction_count": 18,
        "line_count": 57,
        "load_store_count": 0,
        "stack_ops_count": 0,
        "text_section_bytes": 1478,
        "variant": "C-P8-O2"
      },
      "O3": {
        "binary_size_bytes": 15960,
        "branch_count": 1,
        "call_count": 1,
        "cond_branch_count": 1,
        "instruction_count": 18,
        "line_count": 57,
        "load_store_count": 0,
        "stack_ops_count": 0,
        "text_section_bytes": 1478,
        "variant": "C-P8-O3"
      }
    },
    "s3": {
      "H4": {
        "O0": {
          "binary_size_bytes": 51160,
          "branch_count": 590,
          "call_count": 41,
          "cond_branch_count": 289,
          "instruction_count": 2565,
          "line_count": 3565,
          "load_store_count": 1133,
          "stack_ops_count": 386,
          "text_section_bytes": 36033,
          "variant": "H4-P8-O0"
        },
        "O1": {
          "binary_size_bytes": 50960,
          "branch_count": 590,
          "call_count": 41,
          "cond_branch_count": 289,
          "instruction_count": 2583,
          "line_count": 3583,
          "load_store_count": 1151,
          "stack_ops_count": 450,
          "text_section_bytes": 36146,
          "variant": "H4-P8-O1"
        }
      },
      "H5": {
        "O0": {
          "binary_size_bytes": 51160,
          "branch_count": 590,
          "call_count": 41,
          "cond_branch_count": 289,
          "instruction_count": 2565,
          "line_count": 3565,
          "load_store_count": 1133,
          "stack_ops_count": 386,
          "text_section_bytes": 36033,
          "variant": "H5-P8-O0"
        },
        "O1": {
          "binary_size_bytes": 50960,
          "branch_count": 590,
          "call_count": 41,
          "cond_branch_count": 289,
          "instruction_count": 2583,
          "line_count": 3583,
          "load_store_count": 1151,
          "stack_ops_count": 450,
          "text_section_bytes": 36146,
          "variant": "H5-P8-O1"
        }
      }
    }
  },
  "summaries": [
    {
      "checkpoint": "C",
      "count": 30,
      "iqr": 2057.27685546875,
      "mad": 1128.689453125,
      "max": 20408.74609375,
      "mean": 8804.855859375,
      "median": 8301.560546875,
      "min": 5827.13671875,
      "p25": 7279.33740234375,
      "p75": 9336.6142578125,
      "variant": "O0"
    },
    {
      "checkpoint": "C",
      "count": 30,
      "iqr": 2065.580078125,
      "mad": 1194.6123046875,
      "max": 42067.55078125,
      "mean": 9481.959244791668,
      "median": 8288.69140625,
      "min": 5679.580078125,
      "p25": 7082.09716796875,
      "p75": 9147.67724609375,
      "variant": "O2"
    },
    {
      "checkpoint": "C",
      "count": 30,
      "iqr": 2571.85888671875,
      "mad": 1486.861328125,
      "max": 13646.224609375,
      "mean": 8694.9322265625,
      "median": 8652.6337890625,
      "min": 5520.890625,
      "p25": 7161.80029296875,
      "p75": 9733.6591796875,
      "variant": "O3"
    },
    {
      "checkpoint": "H4",
      "count": 30,
      "iqr": 1548.6748046875,
      "mad": 774.0068359375,
      "max": 10477.6484375,
      "mean": 6504.858203125,
      "median": 6320.94140625,
      "min": 4600.572265625,
      "p25": 5631.02978515625,
      "p75": 7179.70458984375,
      "variant": "O0"
    },
    {
      "checkpoint": "H4",
      "count": 30,
      "iqr": 1256.38427734375,
      "mad": 658.275390625,
      "max": 8799.82421875,
      "mean": 6524.641276041667,
      "median": 6555.2685546875,
      "min": 4611.099609375,
      "p25": 5831.943359375,
      "p75": 7088.32763671875,
      "variant": "O1"
    },
    {
      "checkpoint": "H5",
      "count": 30,
      "iqr": 1774.2109375,
      "mad": 873.447265625,
      "max": 11141.380859375,
      "mean": 6526.176953125,
      "median": 6294.056640625,
      "min": 4528.083984375,
      "p25": 5551.75048828125,
      "p75": 7325.96142578125,
      "variant": "O0"
    },
    {
      "checkpoint": "H5",
      "count": 30,
      "iqr": 1225.10302734375,
      "mad": 627.3037109375,
      "max": 9302.033203125,
      "mean": 6643.151432291666,
      "median": 6721.1357421875,
      "min": 4434.521484375,
      "p25": 6044.3349609375,
      "p75": 7269.43798828125,
      "variant": "O1"
    }
  ],
  "workload": "P8"
}
