# Benchmarking Python Extensions
A quick project to compare the performance of Python, Cython, Julia, and Rust on certain tasks.
The goal is to show that depending on the problem, you can write a Python extension in another language to speed up the code. 
In some cases the difference is significant, in other cases, the overhead of calling the extension is too high.
In all cases it is cumbersome to write and maintain the extension code, so it should be done only when necessary to address critical bottlenecks.

**NOTE:** These algorithms are not necessarily the most optimal implementations, they are meant to be simple and easy to compare across languages.

## Results: 

Notes: 
- All times are in microseconds
- Each configuration runs a loop of X iterations through every example for the problem.
  - For slower problems, we do less iterations to avoid taking too long.  
- The diff_ratio is the difference in execution time between pure Python and the other implementations.

 | task                | lang           |     avg_time |   std_deviation |   iterations |   diff_ratio |
|:--------------------|:---------------|-------------:|----------------:|-------------:|-------------:|
| bigram              | python         |      308.415 |         21.8851 |         1000 |          nan |
| **bigram**          | **cython**         |       235.89 |         17.2207 |         1000 |    -0.235153 |
| bigram              | rust           |      325.695 |         27.3602 |         1000 |    0.0560278 |
| bigram              | julia          |      542.354 |         3883.27 |         1000 |      0.75852 |
| two_sum_n_squared   | python         |       3397.6 |         59.9261 |          100 |          nan |
| two_sum_n_squared   | cython         |      2574.51 |         55.0505 |          100 |    -0.242255 |
| **two_sum_n_squared**   | **rust**           |      254.234 |         9.44736 |          100 |    -0.925172 |
| two_sum_n_squared   | julia          |        48973 |         53175.7 |          100 |       13.414 |
| two_sum_n           | python         |      529.449 |         24.7108 |         1000 |          nan |
| two_sum_n           | cython         |      418.123 |         25.1149 |         1000 |    -0.210267 |
| two_sum_n           | rust           |      298.213 |         24.1917 |         1000 |    -0.436748 |
| **two_sum_n**           | **rust+hashbrown** |      255.792 |         22.6785 |         1000 |    -0.516872 |
| two_sum_n           | julia          |      3373.33 |         12445.6 |          100 |       5.3714 |
| fibonacci_recursive | python         |       371314 |         1502.15 |          100 |          nan |
| fibonacci_recursive | cython         |       197975 |          1899.9 |          100 |    -0.466826 |
| **fibonacci_recursive** | **rust**           |        14856 |         262.095 |          100 |    -0.959991 |
| fibonacci_recursive | julia          |      20494.2 |         192.149 |          100 |    -0.944806 |
| fibonacci_hash      | python         |      26.4787 |          14.414 |         1000 |          nan |
| fibonacci_hash      | cython         |      13.9276 |         9.41323 |         1000 |    -0.474007 |
| fibonacci_hash      | rust           |      6.26339 |         1.59288 |         1000 |    -0.763456 |
| **fibonacci_hash**      | **rust+hashbrown** |      5.09139 |         3.24083 |         1000 |    -0.807717 |
| fibonacci_hash      | julia          |      61.8679 |         1071.35 |         1000 |      1.33651 | 

## How to run the benchmarks
1) Create a virtual environment at `./.venv` and activate it
2) Install requirements: `poetry install`
3) Running `make all` will perform all the setup (including compiling code and building extensions), run the benchmarks, generate a results table, and clean up the added files.

There are more fine-grained commands available in the Makefile for development purposes.
