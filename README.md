# Benchmarking Python Extensions

A quick project to compare the performance of Python, Cython, Julia, and Rust on certain tasks.
The goal is to show that depending on the problem, you can write a Python extension in another language to speed up the code.
In some cases the difference is significant, in other cases, the overhead of calling the extension is too high.
In all cases it is cumbersome to write and maintain the extension code, so it should be done only when necessary to address critical bottlenecks.

**NOTE:** These algorithms are not necessarily the most optimal implementations, they are meant to be simple and easy to compare across languages.

## Results

Notes:

- All times are in microseconds
- Each configuration runs a loop of X iterations through every example for the problem.
  - For slower problems, we do less iterations to avoid taking too long.  
- The diff_ratio is the difference in execution time between pure Python and the other implementations.

Results:

Results:

|    | task                | lang           |     avg_time |   median_time |   std_deviation |   iterations |   dropoff_ratio |   diff_ratio |   diff_ratio_median |
|---:|:--------------------|:---------------|-------------:|--------------:|----------------:|-------------:|----------------:|-------------:|--------------------:|
|  0 | bigram              | python         |    287.465   |       286.334 |       11.4674   |         1000 |     -0.177852   |   nan        |         nan         |
|  1 | bigram              | cython         |    203.777   |       199.791 |       14.0091   |         1000 |     -0.021159   |    -0.291125 |          -0.302245  |
|  2 | bigram              | rust           |    180.285   |       176.583 |       22.1139   |         1000 |     -0.23721    |    -0.372846 |          -0.383297  |
|  3 | bigram              | julia          |    495.474   |       309.833 |     2566        |         1000 |     -0.293304   |     0.723599 |           0.0820685 |
|  4 | two_sum_n_squared   | python         |   3098.19    |      3074.62  |       53.1219   |          100 |     -0.070813   |   nan        |         nan         |
|  5 | two_sum_n_squared   | cython         |   2412.63    |      2396.54  |       31.8206   |          100 |     -0.0320444  |    -0.221278 |          -0.220542  |
|  6 | two_sum_n_squared   | rust           |    224.87    |       222.792 |        8.45196  |          100 |     -0.0908531  |    -0.927419 |          -0.927538  |
|  7 | two_sum_n_squared   | julia          |  51954       |     25601     |    54804.3      |          100 |      0.0799862  |    15.7691   |           7.32654   |
|  8 | two_sum_n           | python         |    402.555   |       400.708 |        7.27904  |         1000 |     -0.116725   |   nan        |         nan         |
|  9 | two_sum_n           | cython         |    325.808   |       324.458 |        9.67103  |         1000 |     -0.0456977  |    -0.190649 |          -0.190288  |
| 10 | two_sum_n           | rust           |    265.727   |       263.208 |        9.57105  |         1000 |     -0.145544   |    -0.339899 |          -0.343143  |
| 11 | two_sum_n           | rust+hashbrown |    229.437   |       227.083 |        9.12063  |         1000 |     -0.0505625  |    -0.430049 |          -0.433296  |
| 12 | two_sum_n           | julia          |   3161.93    |      1511.38  |    12691.7      |          100 |     -0.0796766  |     6.85465  |           2.77176   |
| 13 | fibonacci_recursive | python         | 296866       |    293776     |    13943.3      |          100 |      0.0046769  |   nan        |         nan         |
| 14 | fibonacci_recursive | cython         | 226095       |    225052     |     9258.93     |          100 |     -0.00655737 |    -0.238394 |          -0.233931  |
| 15 | fibonacci_recursive | rust           |      1.51336 |         1.167 |        2.3015   |          100 |     -0.877331   |    -0.999995 |          -0.999996  |
| 16 | fibonacci_recursive | julia          |  20983.7     |     20906.6   |      170.94     |          100 |      0.00321722 |    -0.929316 |          -0.928835  |
| 17 | fibonacci_hash      | python         |     14.3003  |        12.333 |       14.3049   |         1000 |     -0.270258   |   nan        |         nan         |
| 18 | fibonacci_hash      | cython         |      8.78437 |         7.458 |        9.44596  |         1000 |      4.40903    |    -0.385723 |          -0.395281  |
| 19 | fibonacci_hash      | rust           |      3.79137 |         3.708 |        1.0044   |         1000 |     -0.568187   |    -0.734876 |          -0.699343  |
| 20 | fibonacci_hash      | rust+hashbrown |      2.51913 |         2.5   |        0.543433 |         1000 |     -0.537346   |    -0.823841 |          -0.797292  |
| 21 | fibonacci_hash      | julia          |     59.8857  |        25.459 |     1070.7      |         1000 |     -0.64077    |     3.18771  |           1.0643    |

## How to run the benchmarks

1) Create a virtual environment at `./.venv` and activate it
2) Install requirements: `poetry install`
3) Running `make all` will perform all the setup (including compiling code and building extensions), run the benchmarks, generate a results table, and clean up the added files.

There are more fine-grained commands available in the Makefile for development purposes.
