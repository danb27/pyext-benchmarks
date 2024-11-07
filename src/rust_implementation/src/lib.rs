use std::collections::HashMap;
use hashbrown::HashMap as HBHashMap;
use pyo3::prelude::*;

#[pyfunction]
fn bigrams(text: &str) -> PyResult<Vec<String>> {
    // Pre-split and collect to avoid multiple allocations
    let words: Vec<_> = text.split_whitespace().collect();
    let len = words.len();
    
    if len < 2 {
        return Ok(Vec::new());
    }
    
    // Single allocation with exact capacity
    let mut bigrams = Vec::with_capacity(len - 1);
    
    // Use windows for more efficient iteration
    words.windows(2)
        .for_each(|pair| {
            // Avoid separate format! allocation by using with_capacity
            let mut s = String::with_capacity(pair[0].len() + pair[1].len() + 1);
            s.push_str(pair[0]);
            s.push(' ');
            s.push_str(pair[1]);
            bigrams.push(s);
        });

    Ok(bigrams)
}

#[pyfunction]
fn two_sum_n_squared(nums: Vec<i32>, target: i32) -> PyResult<Vec<i32>> {
    let len = nums.len();
    if len < 2 {
        return Ok(Vec::new());
    }
    
    // Use unchecked access for better performance in release mode
    unsafe {
        for i in 0..len-1 {
            let num_i = *nums.get_unchecked(i);
            let needed = target - num_i;
            
            // SIMD-friendly sequential access
            for j in (i + 1)..len {
                if *nums.get_unchecked(j) == needed {
                    return Ok(vec![i as i32, j as i32]);
                }
            }
        }
    }
    
    Ok(Vec::new())
}

#[pyfunction]
fn two_sum_n(nums: Vec<i32>, target: i32) -> PyResult<Vec<i32>> {
    let len = nums.len();
    if len < 2 {
        return Ok(Vec::new());
    }
    
    let mut map = HashMap::with_capacity(len);
    
    // Use iterator for better optimization
    for (i, &num) in nums.iter().enumerate() {
        let complement = target - num;
        
        if let Some(&j) = map.get(&complement) {
            return Ok(vec![j as i32, i as i32]);
        }
        
        map.insert(num, i);
    }
    
    Ok(Vec::new())
}

#[pyfunction]
fn two_sum_n_hashbrown(nums: Vec<i32>, target: i32) -> PyResult<Vec<i32>> {
    let len = nums.len();
    if len < 2 {
        return Ok(Vec::new());
    }
    
    let mut map = HBHashMap::with_capacity(len);
    
    // Avoid bounds checking in release mode
    unsafe {
        for (i, &num) in nums.iter().enumerate() {
            let complement = target - num;
            
            if let Some(&j) = map.get(&complement) {
                return Ok(vec![j as i32, i as i32]);
            }
            
            map.insert(num, i);
        }
    }
    
    Ok(Vec::new())
}

#[pyfunction]
fn fibonacci_recursive(n: i32) -> PyResult<i32> {
    // Use tail recursion optimization
    fn fib_tail(n: i32, a: i32, b: i32) -> i32 {
        match n {
            0 => a,
            1 => b,
            _ => fib_tail(n - 1, b, a + b)
        }
    }
    
    Ok(fib_tail(n, 0, 1))
}

#[pyfunction]
fn fibonacci_hash(n: i32) -> PyResult<i32> {
    if n <= 1 {
        return Ok(n);
    }
    
    let mut map = HashMap::with_capacity((n + 1) as usize);
    map.insert(0, 0);
    map.insert(1, 1);
    
    // Iterative approach is faster than recursive
    for i in 2..=n {
        let val = map.get(&(i-1)).unwrap() + map.get(&(i-2)).unwrap();
        map.insert(i, val);
    }
    
    Ok(*map.get(&n).unwrap())
}

#[pyfunction]
fn fibonacci_hashbrown(n: i32) -> PyResult<i32> {
    if n <= 1 {
        return Ok(n);
    }
    
    let mut map = HBHashMap::with_capacity((n + 1) as usize);
    map.insert(0, 0);
    map.insert(1, 1);
    
    // Iterative approach with minimal HashMap lookups
    for i in 2..=n {
        unsafe {
            let val = map.get(&(i-1)).unwrap_unchecked() + map.get(&(i-2)).unwrap_unchecked();
            map.insert(i, val);
        }
    }
    
    Ok(*map.get(&n).unwrap())
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