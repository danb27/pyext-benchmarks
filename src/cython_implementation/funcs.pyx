#cython_implementation: language_level=3

def bigrams(text: str) -> list[str]:
    cdef list[str] tokens = text.split()
    cdef list[str] bigrams = []
    cdef int i
    for i in range(len(tokens) - 1):
        bigrams.append(f"{tokens[i]} {tokens[i + 1]}")
    return bigrams


def two_sum_n_squared(nums: list[int], target: int) -> list[int]:
    cdef int i, j
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def two_sum_n(nums: list[int], target: int) -> list[int]:
    cdef dict[int, int] num_to_index = {}
    cdef int i
    for i in range(len(nums)):
        if target - nums[i] in num_to_index:
            return [num_to_index[target - nums[i]], i]
        num_to_index[nums[i]] = i
    return []


def fibonacci_recursive(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_hash(n: int) -> int:
    cdef dict[int, int] cache = {0: 0, 1: 1}

    def inner(n: int) -> int:
        if n in cache:
            return cache[n]
        cache[n] = inner(n - 1) + inner(n - 2)
        return cache[n]

    return inner(n)
