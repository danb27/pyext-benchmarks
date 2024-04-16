import pandas as pd

import rust_implementation as rust_funcs
from cython_implementation import funcs as cython_funcs
from data import constants
from python_implementation.funcs import bigrams, two_sum_n_squared, two_sum_n
from runner import BenchmarkRunner


ALL_RUNNERS = {
    "bigram": {
        "python": BenchmarkRunner(
            bigrams, constants.BIGRAM_REQUESTS, constants.BIGRAM_OUTPUTS
        ),
        "cython": BenchmarkRunner(
            cython_funcs.bigrams, constants.BIGRAM_REQUESTS, constants.BIGRAM_OUTPUTS
        ),
        "rust": BenchmarkRunner(
            rust_funcs.bigrams, constants.BIGRAM_REQUESTS, constants.BIGRAM_OUTPUTS
        ),
    },
    "two_sum_n_squared": {
        "python": BenchmarkRunner(
            two_sum_n_squared, constants.TWO_SUM_REQUESTS, constants.TWO_SUM_RESPONSES
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
    },
    "two_sum_n": {
        "python": BenchmarkRunner(
            two_sum_n, constants.TWO_SUM_REQUESTS, constants.TWO_SUM_RESPONSES
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
for task, implementations in ALL_RUNNERS.items():
    for lang, runner in implementations.items():
        print(f"Benchmarking {lang}({task})")
        avg_time, std_deviation = runner.process_all_repeated()
        results.append({"avg_time": avg_time, "std_deviation": std_deviation})
        index.append((task, lang))
        full_results.append(
            {
                "task": task,
                "lang": lang,
                "avg_time": avg_time,
                "std_deviation": std_deviation,
            }
        )
        if lang == "python":
            python_times[task] = avg_time

df = pd.DataFrame(full_results)

df["diff_ratio"] = df.apply(
    lambda row: ((row["avg_time"] / python_times[row["task"]]) - 1 or None), axis=1
)
print("\n\nResults: \n", df.to_markdown(), "\n\n")
