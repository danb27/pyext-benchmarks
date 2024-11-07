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

|    | task                | lang           |     avg_time |   median_time |   std_deviation |   iterations |   dropoff_ratio |   diff_ratio |   diff_ratio_median |
|---:|:--------------------|:---------------|-------------:|--------------:|----------------:|-------------:|----------------:|-------------:|--------------------:|
|  0 | bigram              | python         |    280.712   |       279     |      13.1209    |         1000 |    -0.215146    |   nan        |          nan        |
|  1 | bigram              | cython         |    198.394   |       196.416 |       9.50708   |         1000 |    -0.0649355   |    -0.293247 |           -0.296    |
|  2 | bigram              | rust           |    169.039   |       167.125 |      11.1048    |         1000 |    -0.267381    |    -0.397819 |           -0.400986 |
|  3 | bigram              | julia          |    540.096   |       310.208 |    2916.2       |         1000 |    -0.317572    |     0.924022 |            0.111857 |
|  4 | two_sum_n_squared   | python         |   3138.11    |      3120.12  |      72.6327    |          100 |    -0.0353831   |   nan        |          nan        |
|  5 | two_sum_n_squared   | cython         |   2401.13    |      2390.67  |      26.3401    |          100 |     0.0181195   |    -0.234849 |           -0.233791 |
|  6 | two_sum_n_squared   | rust           |    191.337   |       189.417 |       7.29381   |          100 |    -0.177625    |    -0.939028 |           -0.939292 |
|  7 | two_sum_n_squared   | julia          |  47318.3     |     21008.5   |   54280.6       |          100 |     0.0398841   |    14.0786   |            5.73322  |
|  8 | two_sum_n           | python         |    401.626   |       399.5   |      11.5413    |         1000 |    -0.0764099   |   nan        |          nan        |
|  9 | two_sum_n           | cython         |    325.601   |       324     |       5.67588   |         1000 |    -0.0336123   |    -0.189295 |           -0.188986 |
| 10 | two_sum_n           | rust           |    235.718   |       235.125 |       3.26271   |         1000 |    -0.0294578   |    -0.413091 |           -0.411452 |
| 11 | two_sum_n           | rust+hashbrown |    199.26    |       198.375 |       6.60893   |         1000 |    -0.0290393   |    -0.503867 |           -0.503442 |
| 12 | two_sum_n           | julia          |   2963.39    |      1365.46  |   12561.8       |          100 |    -0.086549    |     6.37847  |            2.41792  |
| 13 | fibonacci_recursive | python         | 292983       |    292465     |    2474.55      |          100 |    -0.000971841 |   nan        |          nan        |
| 14 | fibonacci_recursive | cython         | 225440       |    223774     |    8980         |          100 |    -0.00144737  |    -0.230534 |           -0.234868 |
| 15 | fibonacci_recursive | rust           |      1.23665 |         1.166 |       0.664831  |          100 |    -0.828905    |    -0.999996 |           -0.999996 |
| 16 | fibonacci_recursive | julia          |  20872.9     |     20857     |      84.2607    |          100 |    -0.00112985  |    -0.928757 |           -0.928686 |
| 17 | fibonacci_hash      | python         |     13.9819  |        12.25  |      13.2601    |         1000 |    -0.249445    |   nan        |          nan        |
| 18 | fibonacci_hash      | cython         |      8.35292 |         7.333 |       8.21781   |         1000 |    -0.537045    |    -0.402591 |           -0.401388 |
| 19 | fibonacci_hash      | rust           |      3.73043 |         3.708 |       0.294707  |         1000 |    -0.497442    |    -0.733196 |           -0.697306 |
| 20 | fibonacci_hash      | rust+hashbrown |      2.48002 |         2.459 |       0.0859066 |         1000 |    -0.4         |    -0.822627 |           -0.799265 |
| 21 | fibonacci_hash      | julia          |     59.7029  |        27.334 |    1004.06      |         1000 |    -0.540344    |     3.27001  |            1.23135  |

## How to run the benchmarks

1) Create a virtual environment at `./.venv` and activate it
2) Install requirements: `poetry install`
3) Running `make all` will perform all the setup (including compiling code and building extensions), run the benchmarks, generate a results table, and clean up the added files.

There are more fine-grained commands available in the Makefile for development purposes.
