from juliacall import Main as jl

# Load Julia functions
jl.include("julia_implementation/funcs.jl")


def bigrams(text):
    return jl.bigrams(text=text)


def two_sum_n_squared(nums, target):
    return jl.two_sum_n_squared(nums=nums, target=target)


def two_sum_n(nums, target):
    return jl.two_sum_n(nums=nums, target=target)


fibonacci_recursive = jl.fibonacci_recursive
