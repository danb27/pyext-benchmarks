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
|  0 | bigram              | python         |    224.541   |       224.292 |       13.8099   |         1000 |    -0.341245    |   nan        |          nan        |
|  1 | bigram              | cython         |    156.813   |       156.041 |        4.66363  |         1000 |    -0.0837656   |    -0.301632 |           -0.304295 |
|  2 | bigram              | rust           |    141.109   |       140.083 |        6.38828  |         1000 |    -0.329444    |    -0.371568 |           -0.375444 |
|  3 | bigram              | julia          |    413.931   |       248.583 |     2314.98     |         1000 |    -0.35095     |     0.843451 |            0.108301 |
|  4 | two_sum_n_squared   | python         |   2476.16    |      2474.12  |        9.72675  |          100 |    -0.00748136  |   nan        |          nan        |
|  5 | two_sum_n_squared   | cython         |   1935.69    |      1933.5   |       12.8745   |          100 |    -0.000644923 |    -0.218267 |           -0.218512 |
|  6 | two_sum_n_squared   | rust           |    152.479   |       151.792 |        3.50386  |          100 |    -0.144016    |    -0.938421 |           -0.938648 |
|  7 | two_sum_n_squared   | julia          |  37572.7     |     16625.6   |    43190.3      |          100 |     0.0494449   |    14.1738   |            5.7198   |
|  8 | two_sum_n           | python         |    322.932   |       322.166 |        6.74927  |         1000 |    -0.0786446   |   nan        |          nan        |
|  9 | two_sum_n           | cython         |    249.853   |       247.25  |        6.7387   |         1000 |    -0.0662983   |    -0.226299 |           -0.232539 |
| 10 | two_sum_n           | rust           |    179.636   |       177.958 |        4.68455  |         1000 |    -0.1232      |    -0.443736 |           -0.44762  |
| 11 | two_sum_n           | rust+hashbrown |    151.514   |       150.208 |        3.72531  |         1000 |    -0.0385968   |    -0.530816 |           -0.533756 |
| 12 | two_sum_n           | julia          |   2489.1     |      1103.12  |    10925.5      |          100 |    -0.989429    |     6.70781  |            2.42409  |
| 13 | fibonacci_recursive | python         | 223853       |    222978     |     4066.07     |          100 |     0.112266    |   nan        |          nan        |
| 14 | fibonacci_recursive | cython         | 179109       |    177356     |    10280.2      |          100 |    -0.00726162  |    -0.199883 |           -0.204603 |
| 15 | fibonacci_recursive | rust           |      0.99087 |         0.958 |        0.424193 |          100 |    -0.782272    |    -0.999996 |           -0.999996 |
| 16 | fibonacci_recursive | julia          |  16030.4     |     16049     |      161.038    |          100 |     0.00934993  |    -0.928389 |           -0.928024 |
| 17 | fibonacci_hash      | python         |     10.7123  |         9.292 |       10.3399   |         1000 |    -0.0831296   |   nan        |          nan        |
| 18 | fibonacci_hash      | cython         |      6.48539 |         5.583 |        6.55853  |         1000 |    -0.545239    |    -0.394587 |           -0.399161 |
| 19 | fibonacci_hash      | rust           |      2.79985 |         2.75  |        0.491507 |         1000 |    -0.601047    |    -0.738633 |           -0.704046 |
| 20 | fibonacci_hash      | rust+hashbrown |      1.94032 |         1.917 |        0.242489 |         1000 |    -0.614756    |    -0.818871 |           -0.793693 |
| 21 | fibonacci_hash      | julia          |     49.6897  |        20.708 |      907.932    |         1000 |    -0.629555    |     3.63855  |            1.22858  |

## How to run the benchmarks

1) Create a virtual environment at `./.venv` and activate it
2) Install requirements: `poetry install`
3) Running `make all` will perform all the setup (including compiling code and building extensions), run the benchmarks, generate a results table, and clean up the added files.

There are more fine-grained commands available in the Makefile for development purposes.
