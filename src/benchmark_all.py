import pandas as pd

import rust_implementation as rust_funcs
from cython_implementation import funcs as cython_funcs
from data import constants
from julia_implementation import funcs as julia_funcs
from python_implementation import funcs as py_funcs
from runner import BenchmarkRunner


ALL_RUNNERS = {
    "bigram": {
        "python": BenchmarkRunner(
            py_funcs.bigrams, constants.BIGRAM_REQUESTS, constants.BIGRAM_OUTPUTS
        ),
        "cython": BenchmarkRunner(
            cython_funcs.bigrams, constants.BIGRAM_REQUESTS, constants.BIGRAM_OUTPUTS
        ),
        "rust": BenchmarkRunner(
            rust_funcs.bigrams, constants.BIGRAM_REQUESTS, constants.BIGRAM_OUTPUTS
        ),
        "julia": BenchmarkRunner(
            julia_funcs.bigrams, constants.BIGRAM_REQUESTS, constants.BIGRAM_OUTPUTS
        ),
    },
    "two_sum_n_squared": {
        "python": BenchmarkRunner(
            py_funcs.two_sum_n_squared,
            constants.TWO_SUM_REQUESTS,
            constants.TWO_SUM_RESPONSES,
        ),
        "cython": BenchmarkRunner(
            cython_funcs.two_sum_n_squared,
            constants.TWO_SUM_REQUESTS,
            constants.TWO_SUM_RESPONSES,
        ),
        "rust": BenchmarkRunner(
            rust_funcs.two_sum_n_squared,
            constants.TWO_SUM_REQUESTS,
            constants.TWO_SUM_RESPONSES,
        ),
        "julia": BenchmarkRunner(
            julia_funcs.two_sum_n_squared,
            constants.TWO_SUM_REQUESTS,
            constants.TWO_SUM_RESPONSES,
        ),
    },
    "two_sum_n": {
        "python": BenchmarkRunner(
            py_funcs.two_sum_n, constants.TWO_SUM_REQUESTS, constants.TWO_SUM_RESPONSES
        ),
        "cython": BenchmarkRunner(
            cython_funcs.two_sum_n,
            constants.TWO_SUM_REQUESTS,
            constants.TWO_SUM_RESPONSES,
        ),
        "rust": BenchmarkRunner(
            rust_funcs.two_sum_n,
            constants.TWO_SUM_REQUESTS,
            constants.TWO_SUM_RESPONSES,
        ),
        "rust+hashbrown": BenchmarkRunner(
            rust_funcs.two_sum_n_hashbrown,
            constants.TWO_SUM_REQUESTS,
            constants.TWO_SUM_RESPONSES,
        ),
        "julia": BenchmarkRunner(
            julia_funcs.two_sum_n,
            constants.TWO_SUM_REQUESTS,
            constants.TWO_SUM_RESPONSES,
        ),
    },
    "fibonacci_recursive": {
        "python": BenchmarkRunner(
            py_funcs.fibonacci_recursive,
            constants.FIBONACCI_REQUESTS,
            constants.FIBONACCI_RESPONSES,
        ),
        "cython": BenchmarkRunner(
            cython_funcs.fibonacci_recursive,
            constants.FIBONACCI_REQUESTS,
            constants.FIBONACCI_RESPONSES,
        ),
        "rust": BenchmarkRunner(
            rust_funcs.fibonacci_recursive,
            constants.FIBONACCI_REQUESTS,
            constants.FIBONACCI_RESPONSES,
        ),
        "julia": BenchmarkRunner(
            julia_funcs.fibonacci_recursive,
            constants.FIBONACCI_REQUESTS,
            constants.FIBONACCI_RESPONSES,
        ),
    },
}

# Make sure all runners pass their tests
for task, implementations in ALL_RUNNERS.items():
    for lang, runner in implementations.items():
        print(f"Testing {lang}({task})")
        runner.test_all()

# Benchmark all runners
results = []
index = []
full_results = []
python_times = {k: None for k in ALL_RUNNERS.keys()}
python_median_times = {k: None for k in ALL_RUNNERS.keys()}
for task, implementations in ALL_RUNNERS.items():
    for lang, runner in implementations.items():
        print(f"Benchmarking {lang}({task})")
        avg_time, std_deviation, median, dropoff = runner.process_all_repeated()
        results_dict = {
            "avg_time": avg_time,
            "median_time": median,
            "std_deviation": std_deviation,
            # Dropoff from first iteration to second
            "dropoff_ratio": dropoff,
        }
        results.append(results_dict)
        index.append((task, lang))
        full_results.append(
            {
                "task": task,
                "lang": lang,
            }
            | results_dict
        )
        if lang == "python":
            python_times[task] = avg_time
            python_median_times[task] = median

df = pd.DataFrame(full_results)

df["diff_ratio"] = df.apply(
    lambda row: ((row["avg_time"] / python_times[row["task"]]) - 1 or None), axis=1
)
df["diff_ratio_median"] = df.apply(
    lambda row: ((row["median_time"] / python_median_times[row["task"]]) - 1 or None),
    axis=1,
)
print("\n\nResults: \n", df.to_markdown(), "\n\n")
