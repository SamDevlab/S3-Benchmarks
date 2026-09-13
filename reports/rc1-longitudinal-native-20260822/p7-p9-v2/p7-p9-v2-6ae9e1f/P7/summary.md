# P7 native workload

{
  "control_drift_percent": 361.36850553517775,
  "control_stable": false,
  "control_stats": {
    "count": 30,
    "iqr": 509.72509765625,
    "mad": 205.42724609375,
    "max": 2207.629150390625,
    "mean": 844.4961995442708,
    "median": 698.5994873046875,
    "min": 478.495849609375,
    "p25": 550.1801147460938,
    "p75": 1059.9052124023438
  },
  "correctness": {
    "control_result": 3615354,
    "status": "PASS",
    "variants": {
      "C-O0": 3615354,
      "C-O2": 3615354,
      "C-O3": 3615354,
      "H4-O0": 3615354,
      "H4-O1": 3615354,
      "H5-O0": 3615354,
      "H5-O1": 3615354
    }
  },
  "inputs_pinned": true,
  "name": "native arithmetic control",
  "oracle_defined": true,
  "paired": {
    "rc1_vs_c_o2_percent": [
      -2.967144174667813,
      -3.489206662283584,
      -4.5982640964216,
      -2.3511490216923225,
      -7.629632484007354,
      1.8967029680015957,
      3.1465155670993727,
      -22.339462619160454,
      -1.9763756341986682,
      -4.146031713648901,
      3.816475055953572,
      12.998214475733704,
      36.22339298079782,
      0.48479909652456854,
      77.92551630960259,
      35.50291043498059,
      -12.826757388297716,
      2.647763223654098,
      -4.908667593355842,
      -20.9619119379849,
      -11.288387943479394,
      -0.008022238939298099,
      56.200844111029255,
      4.912586091429549,
      16.227068599315686,
      -18.798583782733324,
      -56.46733534244981,
      35.73693804027407,
      8.577890065578298,
      -9.704947011902298
    ],
    "rc1_vs_m230_percent": [
      4.257277957817651,
      -4.848697174036931,
      -19.0866661079382,
      -8.163422619509165,
      -2.9992223898330006,
      3.891661430829707,
      3.548269886522437,
      2.1983433538115937,
      2.727839312368996,
      -14.972177928001107,
      11.013057075610755,
      12.688141674555942,
      44.41724753752714,
      -6.322138370885777,
      64.23728151005031,
      36.20740886336902,
      0.7786316020317541,
      27.78385879246763,
      17.270953258116517,
      -3.1901180660977024,
      2.6507859655918065,
      -8.917611234924072,
      45.94938422087809,
      0.40432785425335016,
      42.68558340290085,
      -15.417163181246341,
      0.035094959692894,
      66.44041587522256,
      -13.504438396109219,
      26.521189356328968
    ]
  },
  "perf": "DEFERRED_BY_ENVIRONMENT",
  "protocol": {
    "cpu_affinity": "taskset -c 0",
    "operations_per_run": 4096,
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
        "binary_size_bytes": 15984,
        "branch_count": 9,
        "call_count": 2,
        "cond_branch_count": 5,
        "instruction_count": 55,
        "line_count": 110,
        "load_store_count": 0,
        "stack_ops_count": 0,
        "text_section_bytes": 1582,
        "variant": "C-P7-O0"
      },
      "O2": {
        "binary_size_bytes": 15960,
        "branch_count": 10,
        "call_count": 1,
        "cond_branch_count": 7,
        "instruction_count": 38,
        "line_count": 89,
        "load_store_count": 0,
        "stack_ops_count": 0,
        "text_section_bytes": 1526,
        "variant": "C-P7-O2"
      },
      "O3": {
        "binary_size_bytes": 15960,
        "branch_count": 10,
        "call_count": 1,
        "cond_branch_count": 7,
        "instruction_count": 38,
        "line_count": 89,
        "load_store_count": 0,
        "stack_ops_count": 0,
        "text_section_bytes": 1526,
        "variant": "C-P7-O3"
      }
    },
    "s3": {
      "H4": {
        "O0": {
          "binary_size_bytes": 58768,
          "branch_count": 707,
          "call_count": 37,
          "cond_branch_count": 344,
          "instruction_count": 3025,
          "line_count": 4217,
          "load_store_count": 1355,
          "stack_ops_count": 394,
          "text_section_bytes": 46849,
          "variant": "H4-P7-O0"
        },
        "O1": {
          "binary_size_bytes": 58488,
          "branch_count": 707,
          "call_count": 37,
          "cond_branch_count": 344,
          "instruction_count": 3043,
          "line_count": 4235,
          "load_store_count": 1373,
          "stack_ops_count": 482,
          "text_section_bytes": 46969,
          "variant": "H4-P7-O1"
        }
      },
      "H5": {
        "O0": {
          "binary_size_bytes": 58768,
          "branch_count": 707,
          "call_count": 37,
          "cond_branch_count": 344,
          "instruction_count": 3025,
          "line_count": 4217,
          "load_store_count": 1355,
          "stack_ops_count": 394,
          "text_section_bytes": 46849,
          "variant": "H5-P7-O0"
        },
        "O1": {
          "binary_size_bytes": 58488,
          "branch_count": 707,
          "call_count": 37,
          "cond_branch_count": 344,
          "instruction_count": 3043,
          "line_count": 4235,
          "load_store_count": 1373,
          "stack_ops_count": 482,
          "text_section_bytes": 46969,
          "variant": "H5-P7-O1"
        }
      }
    }
  },
  "summaries": [
    {
      "checkpoint": "C",
      "count": 30,
      "iqr": 518.6867065429688,
      "mad": 247.512939453125,
      "max": 1927.3896484375,
      "mean": 845.2849365234375,
      "median": 753.6060791015625,
      "min": 463.1982421875,
      "p25": 555.9771118164062,
      "p75": 1074.663818359375,
      "variant": "O0"
    },
    {
      "checkpoint": "C",
      "count": 30,
      "iqr": 509.72509765625,
      "mad": 205.42724609375,
      "max": 2207.629150390625,
      "mean": 844.4961995442708,
      "median": 698.5994873046875,
      "min": 478.495849609375,
      "p25": 550.1801147460938,
      "p75": 1059.9052124023438,
      "variant": "O2"
    },
    {
      "checkpoint": "C",
      "count": 30,
      "iqr": 475.83349609375,
      "mad": 261.7611083984375,
      "max": 1724.013427734375,
      "mean": 855.4476399739583,
      "median": 849.2957763671875,
      "min": 471.0791015625,
      "p25": 563.2103271484375,
      "p75": 1039.0438232421875,
      "variant": "O3"
    },
    {
      "checkpoint": "H4",
      "count": 30,
      "iqr": 533.4342041015625,
      "mad": 241.2099609375,
      "max": 1367.11376953125,
      "mean": 864.3603190104167,
      "median": 808.9893798828125,
      "min": 514.76025390625,
      "p25": 589.94873046875,
      "p75": 1123.3829345703125,
      "variant": "O0"
    },
    {
      "checkpoint": "H4",
      "count": 30,
      "iqr": 357.7552490234375,
      "mad": 174.53955078125,
      "max": 1235.0087890625,
      "mean": 758.6571207682292,
      "median": 686.526123046875,
      "min": 491.303466796875,
      "p25": 559.9014892578125,
      "p75": 917.65673828125,
      "variant": "O1"
    },
    {
      "checkpoint": "H5",
      "count": 30,
      "iqr": 528.53759765625,
      "mad": 214.3360595703125,
      "max": 1767.02490234375,
      "mean": 875.7145833333333,
      "median": 778.2130126953125,
      "min": 518.820068359375,
      "p25": 595.382080078125,
      "p75": 1123.919677734375,
      "variant": "O0"
    },
    {
      "checkpoint": "H5",
      "count": 30,
      "iqr": 434.51141357421875,
      "mad": 239.561767578125,
      "max": 1766.537353515625,
      "mean": 839.9720703125,
      "median": 841.0599365234375,
      "min": 485.285400390625,
      "p25": 570.4226684570312,
      "p75": 1004.93408203125,
      "variant": "O1"
    }
  ],
  "workload": "P7"
}
