from functools import wraps
from time import perf_counter_ns as perf_counter
from typing import Any, Callable


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        print(f"{func.__name__} took {end - start} ns")
        return result

    return wrapper


def timeit_repeated(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            start = perf_counter()
            for _ in range(n):
                result = func(*args, **kwargs)
            end = perf_counter()
            print(f"{func.__name__} took {(end - start)/n} ns on average")
            return result

        return wrapper

    return decorator


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
            assert str(response) == expected, f"Expected {expected}, but got {response}"

    def process_one(self, **kwargs):
        return self.func(**kwargs)

    def test_all(self):
        for request, expected in zip(self.inputs.values(), self.outputs.values()):
            self.test_one(request, expected)

    def process_all(self):
        return [self.process_one(**request) for request in self.inputs.values()]

    def process_all_repeated(self):
        times = []
        for _ in range(1_000):
            start = perf_counter()
            self.process_all()
            end = perf_counter()
            times.append((end - start) / 10_000)

        avg = sum(times) / len(times)
        std = (sum((t - avg) ** 2 for t in times) / len(times)) ** 0.5
        return avg, std
