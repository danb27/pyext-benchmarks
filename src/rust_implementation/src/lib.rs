use std::collections::HashMap;

use hashbrown::HashMap as HBHashMap;
use pyo3::prelude::*;


#[pyfunction]
fn bigrams(text: &str) -> PyResult<Vec<String>> {
    let tokens: Vec<&str> = text.split_whitespace().collect();
    let mut bigrams = Vec::with_capacity(tokens.len() - 1);

    for i in 0..tokens.len() - 1 {
        bigrams.push(format!("{} {}", tokens[i], tokens[i + 1]));
    }

    Ok(bigrams)
}

#[pyfunction]
fn two_sum_n_squared(nums: Vec<i32>, target: i32) -> PyResult<Vec<i32>> {
    for i in 0..nums.len() {
        for j in i + 1..nums.len() {
            if nums[i] + nums[j] == target {
                return Ok(vec![i as i32, j as i32]);
            }
        }
    }

    Ok(vec![])
}

#[pyfunction]
fn two_sum_n(nums: Vec<i32>, target: i32) -> PyResult<Vec<i32>> {
    let mut map = HashMap::with_capacity(nums.len());

    for (i, num) in nums.iter().enumerate() {
        let complement = target - num;

        if let Some(&j) = map.get(&complement) {
            return Ok(vec![j as i32, i as i32]);
        }

        map.insert(num, i);
    }

    Ok(vec![])
}

#[pyfunction]
fn two_sum_n_hashbrown(nums: Vec<i32>, target: i32) -> PyResult<Vec<i32>> {
    let mut map = HBHashMap::with_capacity(nums.len());

    for (i, num) in nums.iter().enumerate() {
        let complement = target - num;

        if let Some(&j) = map.get(&complement) {
            return Ok(vec![j as i32, i as i32]);
        }

        map.insert(num, i);
    }

    Ok(vec![])
}

#[pyfunction]
fn fibonacci_recursive(n: i32) -> PyResult<i32> {
    if n <= 1 {
        return Ok(n);
    }

    Ok(fibonacci_recursive(n - 1)? + fibonacci_recursive(n - 2)?)
}

#[pyfunction]
fn fibonacci_hash(n: i32) -> PyResult<i32> {
    let mut map: HashMap<i32, i32> = HashMap::new();

    fn fib(n: i32, map: &mut HashMap<i32, i32>) -> i32 {
        if n <= 1 {
            return n;
        }

        if let Some(&val) = map.get(&n) {
            return val;
        }

        let val = fib(n - 1, map) + fib(n - 2, map);
        map.insert(n, val);
        val
    }

    let result = fib(n, &mut map);
    Ok(result)
}

#[pyfunction]
fn fibonacci_hashbrown(n: i32) -> PyResult<i32> {
    let mut map: HBHashMap<i32, i32> = HBHashMap::new();

    fn fib(n: i32, map: &mut HBHashMap<i32, i32>) -> i32 {
        if n <= 1 {
            return n;
        }

        if let Some(&val) = map.get(&n) {
            return val;
        }

        let val = fib(n - 1, map) + fib(n - 2, map);
        map.insert(n, val);
        val
    }

    let result = fib(n, &mut map);
    Ok(result)
}

/// A Python module implemented in Rust.
#[pymodule]
fn rust_implementation(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(bigrams, m)?)?;
    m.add_function(wrap_pyfunction!(two_sum_n_squared, m)?)?;
    m.add_function(wrap_pyfunction!(two_sum_n, m)?)?;
    m.add_function(wrap_pyfunction!(two_sum_n_hashbrown, m)?)?;
    m.add_function(wrap_pyfunction!(fibonacci_recursive, m)?)?;
    m.add_function(wrap_pyfunction!(fibonacci_hash, m)?)?;
    m.add_function(wrap_pyfunction!(fibonacci_hashbrown, m)?)?;
    Ok(())
}
