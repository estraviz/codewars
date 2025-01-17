fn merge_arrays(arr1: &[i32], arr2: &[i32]) -> Vec<i32> {
    let mut s: Vec<i32> = [arr1, arr2].concat();
    s.sort();
    s.dedup();
    s
}

#[cfg(test)]
mod tests {
    use super::merge_arrays;

    const ERR_MSG: &str = "\nYour result (left) did not match the expected output (right)";

    fn dotest(a: &[i32], b: &[i32], expected: &[i32]) {
        assert_eq!(
            merge_arrays(a, b),
            expected,
            "{ERR_MSG} with arr1 = {a:?}, arr2 = {b:?}"
        )
    }

    #[test]
    fn sample_tests() {
        dotest(&[1, 2, 3, 4], &[5, 6, 7, 8], &[1, 2, 3, 4, 5, 6, 7, 8]);
        dotest(
            &[1, 3, 5, 7, 9],
            &[10, 8, 6, 4, 2],
            &[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        );
        dotest(
            &[1, 3, 5, 7, 9, 11, 12],
            &[1, 2, 3, 4, 5, 10, 12],
            &[1, 2, 3, 4, 5, 7, 9, 10, 11, 12],
        );
    }
}
