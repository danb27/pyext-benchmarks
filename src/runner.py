from ast import literal_eval
from time import perf_counter_ns
from typing import Any, Callable


class BenchmarkRunner:
    def __init__(self, func, inputs: dict[str, dict], outputs: dict[str, Any]):
        self.func = func
        self.inputs = inputs
        self.outputs = outputs
        # Check for any differences between the keys in texts and outputs
        assert set(self.inputs.keys()) == set(self.outputs.keys())

    def test_one(self, request: dict, expected: Any):
        response = self.process_one(**request)
        if isinstance(expected, Callable):
            assert expected(response, **request)
        else:
            assert response == literal_eval(
                expected
            ), f"Expected {expected}, but got {response} type({type(response)} vs. {type(expected)}) size({len(response)} vs. {len(expected)})"

    def process_one(self, **kwargs):
        return self.func(**kwargs)

    def test_all(self):
        for request, expected in zip(self.inputs.values(), self.outputs.values()):
            self.test_one(request, expected)

    def process_all(self):
        return [self.process_one(**request) for request in self.inputs.values()]

    def process_all_repeated(self):
        times = []
        n = 1_000
        for _ in range(n):
            start = perf_counter_ns()
            self.process_all()
            end = perf_counter_ns()
            # convert nanoseconds to microseconds
            duration = (end - start) / len(self.inputs) / 1_000
            times.append(duration)

        avg = sum(times) / len(times)
        std = (sum((t - avg) ** 2 for t in times) / len(times)) ** 0.5
        median = sorted(times)[len(times) // 2]
        # diff from first iteration to second
        initial_dropoff = (times[1] - times[0]) / times[0]

        return avg, std, median, initial_dropoff
