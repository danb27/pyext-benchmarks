# Benchmarking Python Extensions
A quick project to compare the performance of Python, Cython and Rust on certain tasks.
The goal is to show that depending on the problem, you can write a Python extension in another language to speed up the code. 
In some cases the difference is significant, in other cases, the overhead of calling the extension is too high.
In all cases it is cumbersome to write and maintain the extension code, so it should be done only when necessary to address critical bottlenecks.

**NOTE:** These algorithms are not necessarily the most optimal implementations, they are meant to be simple and easy to compare across languages.

## Results: 

(All times are in nanoseconds)

 |    | task              | lang           |   avg_time |   std_deviation |   diff_ratio |
|---:|:------------------|:---------------|-----------:|----------------:|-------------:|
|  0 | bigram            | python         |    31.0871 |         2.47976 |   nan        |
|  1 | bigram            | cython         |    24.0044 |         1.21291 |    -0.227833 |
|  2 | bigram            | rust           |    34.5862 |         2.74125 |     0.112559 |
|  3 | two_sum_n_squared | python         |   690.067  |        28.8119  |   nan        |
|  4 | two_sum_n_squared | cython         |   494.495  |        17.8117  |    -0.28341  |
|  5 | two_sum_n_squared | rust           |    39.9105 |         2.71808 |    -0.942164 |
|  6 | two_sum_n         | python         |    69.9991 |         3.36944 |   nan        |
|  7 | two_sum_n         | cython         |    53.0215 |         2.28601 |    -0.24254  |
|  8 | two_sum_n         | rust           |    44.0319 |         2.11433 |    -0.370965 |
|  9 | two_sum_n         | rust+hashbrown |    39.0061 |         2.11281 |    -0.442762 |  

## How to run the benchmarks
1) Create a virtual environment at `./.venv` and activate it
2) Install requirements: `poetry install`
3) Running `make all` will perform all the setup (including compiling code and building extensions), run the benchmarks, generate a results table, and clean up the added files.

There are more fine-grained commands available in the Makefile for development purposes.
