use std::collections::HashMap;
use hashbrown::HashMap as HBHashMap;
use pyo3::prelude::*;

#[pyfunction]
fn bigrams(text: &str) -> PyResult<Vec<String>> {
    let words: Vec<_> = text.split_whitespace().collect();
    let len = words.len();
    
    if len < 2 {
        return Ok(Vec::new());
    }
    
    let mut bigrams = Vec::with_capacity(len - 1);
    
    words.windows(2)
        .for_each(|pair| {
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
    
    for i in 0..len-1 {
        let num_i = nums[i];
        let needed = target - num_i;
        
        for j in (i + 1)..len {
            if nums[j] == needed {
                return Ok(vec![i as i32, j as i32]);
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
fn fibonacci_recursive(n: i32) -> PyResult<i32> {
    if n < 0 {
        return Ok(0);
    }
    
    #[inline(always)]
    fn fib_pair(n: i32) -> (i32, i32) {
        match n {
            0 => (0, 1),
            n => {
                let k = n / 2;
                let (fk, fk1) = fib_pair(k);
                let fk2 = fk * (2 * fk1 - fk);
                let fk3 = fk * fk + fk1 * fk1;
                if n % 2 == 0 {
                    (fk2, fk3)
                } else {
                    (fk3, fk2 + fk3)
                }
            }
        }
    }
    
    Ok(fib_pair(n).0)
}

#[pyfunction]
fn fibonacci_hash(n: i32) -> PyResult<i32> {
    if n <= 1 {
        return Ok(n);
    }
    
    let mut map = HashMap::with_capacity((n + 1) as usize);
    map.insert(0, 0);
    map.insert(1, 1);
    
    for i in 2..=n {
        if let (Some(&a), Some(&b)) = (map.get(&(i-1)), map.get(&(i-2))) {
            map.insert(i, a + b);
        }
    }
    
    map.get(&n).copied().ok_or_else(|| PyErr::new::<pyo3::exceptions::PyValueError, _>("Failed to compute fibonacci"))
}

#[pyfunction]
fn fibonacci_hashbrown(n: i32) -> PyResult<i32> {
    if n <= 1 {
        return Ok(n);
    }
    
    let mut map = HBHashMap::with_capacity((n + 1) as usize);
    map.insert(0, 0);
    map.insert(1, 1);
    
    for i in 2..=n {
        if let (Some(&a), Some(&b)) = (map.get(&(i-1)), map.get(&(i-2))) {
            map.insert(i, a + b);
        }
    }
    
    map.get(&n).copied().ok_or_else(|| PyErr::new::<pyo3::exceptions::PyValueError, _>("Failed to compute fibonacci"))
}

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