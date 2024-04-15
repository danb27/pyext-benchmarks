# Benchmarking Python Extensions
A quick project to compare the performance of Python, Cython and Rust on certain tasks.
The goal is to show that depending on the problem, you can write a Python extension in another language to speed up the code. 
In some cases the difference is significant, in other cases, the overhead of calling the extension is too high.
In all cases it is cumbersome to write and maintain the extension code, so it should be done only when necessary to address critical bottlenecks.

**NOTE:** These algorithms are not necessarily the most optimal implementations, they are meant to be simple and easy to compare across languages.

## Results: 

(All times are in nanoseconds)

 |    | task              | lang   |   avg_time |   std_deviation |   diff_ratio |
|---:|:------------------|:-------|-----------:|----------------:|-------------:|
|  0 | bigram            | python |    30.0361 |         1.66569 |   nan        |
|  1 | bigram            | cython |    23.7656 |         1.22293 |    -0.208768 |
|  2 | bigram            | rust   |    33.5566 |         1.9715  |     0.117208 |
|  3 | two_sum_n_squared | python |   655.498  |        14.7438  |   nan        |
|  4 | two_sum_n_squared | cython |   467.766  |        14.9997  |    -0.286396 |
|  5 | two_sum_n_squared | rust   |    38.8923 |         1.57904 |    -0.940668 |
|  6 | two_sum_n         | python |    68.5163 |         3.29455 |   nan        |
|  7 | two_sum_n         | cython |    53.8743 |         2.20422 |    -0.213701 |
|  8 | two_sum_n         | rust   |    52.1785 |         2.47055 |    -0.238451 | 

## How to run the benchmarks
1) Create a virtual environment at `./.venv` and activate it
2) Install requirements: `poetry install`
3) Running `make all` will perform all the setup (including compiling code and building extensions), run the benchmarks, generate a results table, and clean up the added files.

There are more fine-grained commands available in the Makefile for development purposes.
