fn square_or_square_root(arr: &[u32]) -> Vec<u32> {
    arr.iter()
        .map(|num| {
            let root: f64 = (*num as f64).sqrt().floor() as f64;
            let res_elem: u32 = match f64::from(root * root) == (*num as f64) {
                true => root as u32,
                _ => num * num,
            };
            res_elem
        })
        .collect()
}

#[cfg(test)]
mod tests {
    use super::square_or_square_root;

    fn dotest(arr: &[u32], expected: &[u32]) {
        let actual = square_or_square_root(arr);
        assert!(
            actual == expected,
            "Test failed with  arr = {arr:?}\nExpected {expected:?} but got {actual:?}"
        );
    }

    #[test]
    fn sample_tests() {
        dotest(&[4, 3, 9, 7, 2, 1], &[2, 9, 3, 49, 4, 1]);
        dotest(&[100, 101, 5, 5, 1, 1], &[10, 10201, 25, 25, 1, 1]);
        dotest(&[1, 2, 3, 4, 5, 6], &[1, 4, 9, 2, 25, 36]);
    }
}
