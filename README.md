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

 |    | task                | lang           |     avg_time |   std_deviation |   iterations |   diff_ratio |
|---:|:--------------------|:---------------|-------------:|----------------:|-------------:|-------------:|
|  0 | bigram              | python         |    273.206   |       17.853    |         1000 |   nan        |
|  1 | **bigram**              | **cython**         |    189.854   |       16.8827   |         1000 |    -0.305087 |
|  2 | bigram              | rust           |    201.488   |       26.3962   |         1000 |    -0.262506 |
|  3 | bigram              | julia          |    327.528   |     1212        |         1000 |     0.198833 |
|  4 | two_sum_n_squared   | python         |   3060.56    |       66.978    |          100 |   nan        |
|  5 | two_sum_n_squared   | cython         |   1921.73    |       95.2779   |          100 |    -0.372099 |
|  6 | **two_sum_n_squared**   | **rust**           |    212.826   |        8.75903  |          100 |    -0.930462 |
|  7 | two_sum_n_squared   | julia          |  46185       |    91338.6      |          100 |    14.0904   |
|  8 | two_sum_n           | python         |    456.208   |       18.2047   |         1000 |   nan        |
|  9 | two_sum_n           | cython         |    353.863   |       17.4524   |         1000 |    -0.22434  |
| 10 | two_sum_n           | rust           |    261.381   |       21.8427   |         1000 |    -0.427058 |
| 11 | **two_sum_n**           | **rust+hashbrown** |    223.463   |       12.7598   |         1000 |    -0.510174 |
| 12 | two_sum_n           | julia          |   1779.95    |      185.172    |          100 |     2.90163  |
| 13 | fibonacci_recursive | python         | 312024       |     2158.29     |          100 |   nan        |
| 14 | fibonacci_recursive | cython         | 226090       |     8050.41     |          100 |    -0.275408 |
| 15 | **fibonacci_recursive** | **rust**           |  14582.1     |      910.984    |          100 |    -0.953266 |
| 16 | fibonacci_recursive | julia          |  20804.7     |      408.338    |          100 |    -0.933323 |
| 17 | fibonacci_hash      | python         |     18.7462  |       12.9063   |         1000 |   nan        |
| 18 | fibonacci_hash      | cython         |     10.4816  |        7.78693  |         1000 |    -0.440866 |
| 19 | fibonacci_hash      | rust           |      3.87548 |        0.940774 |         1000 |    -0.793266 |
| 20 | **fibonacci_hash**      | **rust+hashbrown** |      2.86238 |        1.52898  |         1000 |    -0.847309 |
| 21 | fibonacci_hash      | julia          |     26.7367  |       22.3975   |         1000 |     0.426244 |


## How to run the benchmarks

1) Create a virtual environment at `./.venv` and activate it
2) Install requirements: `poetry install`
3) Running `make all` will perform all the setup (including compiling code and building extensions), run the benchmarks, generate a results table, and clean up the added files.

There are more fine-grained commands available in the Makefile for development purposes.
