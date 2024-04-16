# Benchmarking Python Extensions
A quick project to compare the performance of Python, Cython and Rust on certain tasks.
The goal is to show that depending on the problem, you can write a Python extension in another language to speed up the code. 
In some cases the difference is significant, in other cases, the overhead of calling the extension is too high.
In all cases it is cumbersome to write and maintain the extension code, so it should be done only when necessary to address critical bottlenecks.

**NOTE:** These algorithms are not necessarily the most optimal implementations, they are meant to be simple and easy to compare across languages.

## Results: 

Notes: 
- All times are in microseconds
- Each configuration runs a loop of 1000 iterations through every example for the problem.
- The time for each run is the average execution time per example.
- The dropoff ratio is the difference in execution time between the first and second iteration.
- The diff_ratio is the difference in execution time between pure Python and the other implementations.

 |    | task              | lang           |   avg_time |   median_time | std_deviation | dropoff_ratio |    diff_ratio | diff_ratio_median |
|---:|:------------------|:---------------|-----------:|--------------:|--------------:|--------------:|--------------:|------------------:|
|  0 | bigram            | python         |   76.478   |      74.6158  |       5.25559 |     -0.174932 |           nan |               nan |
|  1 | bigram            | cython         |   61.0714  |      59.71    |       4.04654 |    -0.0842259 |     -0.201451 |         -0.199767 |
|  2 | bigram            | rust           |   82.8022  |      80.131   |       10.2181 | **-0.417715** | **0.0826931** |     **0.0739154** |
|  3 | bigram            | julia          |  196.488   |     100.703   |   **1213.67** |     -0.117221 |   **1.56921** |      **0.349615** |
|  4 | two_sum_n_squared | python         |   66.5019  |      66.402   |       1.91578 |   -0.00174258 |           nan |               nan |
|  5 | two_sum_n_squared | cython         |   47.8642  |      47.7648  |       2.03739 |      0.057461 |     -0.280259 |         -0.280673 |
|  6 | two_sum_n_squared | rust           |    3.96982 |       3.91077 |      0.204936 |    -0.0331282 |     -0.940305 |         -0.941105 |
|  7 | two_sum_n_squared | julia          |  978.93    |     449.603   |   **675.497** |  **-0.45259** |   **13.7203** |       **5.77092** |
|  8 | two_sum_n         | python         |    6.79214 |       6.73089 |      0.264248 |    -0.0682094 |           nan |               nan |
|  9 | two_sum_n         | cython         |    5.46378 |       5.40208 |      0.230554 |    -0.0797297 |     -0.195574 |          -0.19742 |
| 10 | two_sum_n         | rust           |    4.4296  |       4.36322 |      0.221771 |  **-0.24146** |     -0.347835 |         -0.351762 |
| 11 | two_sum_n         | rust+hashbrown |    3.91807 |       3.84966 |      0.239989 |    -0.0100083 |     -0.423147 |         -0.428061 |
| 12 | two_sum_n         | julia          |   27.176   |      16.89    |   **68.8054** |    -0.0148399 |   **3.00109** |       **1.50933** | 

## How to run the benchmarks
1) Create a virtual environment at `./.venv` and activate it
2) Install requirements: `poetry install`
3) Running `make all` will perform all the setup (including compiling code and building extensions), run the benchmarks, generate a results table, and clean up the added files.

There are more fine-grained commands available in the Makefile for development purposes.
