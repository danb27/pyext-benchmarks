from ast import literal_eval
from time import perf_counter_ns
from typing import Any, Callable

from tqdm import tqdm


class BenchmarkRunner:
    def __init__(
        self, func, inputs: dict[str, dict], outputs: dict[str, Any], n: int = 1_000
    ):
        self.func = func
        self.inputs = inputs
        self.outputs = outputs
        self.n = n
        # Check for any differences between the keys in texts and outputs
        assert set(self.inputs.keys()) == set(self.outputs.keys())

    def test_one(self, request: dict, expected: Any):
        response = self.process_one(**request)
        if isinstance(expected, Callable):
            assert expected(response, **request)
        else:
            if isinstance(expected, str):
                eval_expected = literal_eval(expected)
                if isinstance(eval_expected, list) and not isinstance(response, list):
                    # For Julia VectorValue's
                    response = list(response)
                assert (
                    response == eval_expected
                ), f"Expected {expected}, but got {response} type({type(response)} vs. {type(expected)}) size({len(response)} vs. {len(expected)})"
            else:
                assert response == expected

    def process_one(self, **kwargs):
        return self.func(**kwargs)

    def test_all(self):
        for request, expected in zip(self.inputs.values(), self.outputs.values()):
            self.test_one(request, expected)

    def process_all(self):
        return [self.process_one(**request) for request in self.inputs.values()]

    def process_all_repeated(self):
        times = []
        for _ in tqdm(
            range(self.n), desc=f"Benchmarking {self.func.__name__}", total=self.n
        ):
            start = perf_counter_ns()
            self.process_all()
            end = perf_counter_ns()
            # convert nanoseconds to microseconds
            duration = (end - start) / 1_000
            times.append(duration)

        avg = sum(times) / len(times)
        std = (sum((t - avg) ** 2 for t in times) / len(times)) ** 0.5
        median = sorted(times)[len(times) // 2]
        # diff from first iteration to second
        initial_dropoff = (times[1] - times[0]) / times[0]

        return avg, std, median, initial_dropoff
