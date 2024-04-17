def bigrams(text: str) -> list[str]:
    tokens = text.split()
    bigrams = []
    for i in range(len(tokens) - 1):
        bigrams.append(f"{tokens[i]} {tokens[i + 1]}")
    return bigrams


def two_sum_n_squared(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def two_sum_n(nums: list[int], target: int) -> list[int]:
    num_to_index = {}
    for i, num in enumerate(nums):
        if target - num in num_to_index:
            return [num_to_index[target - num], i]
        num_to_index[num] = i
    return []


def fibonacci_recursive(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_hash(n: int) -> int:
    cache = {0: 0, 1: 1}

    def inner(n: int):
        if n in cache:  # Base case
            return cache[n]
        # Compute and cache the Fibonacci number
        cache[n] = inner(n - 1) + inner(n - 2)  # Recursive case
        return cache[n]

    return inner(n)
