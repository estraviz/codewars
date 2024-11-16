fn slice_plus_slice(xs: &[i32], ys: &[i32]) -> i32 {
    [xs, ys].concat().iter().sum()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn sample_tests() {
        assert_eq!(slice_plus_slice(&vec![1], &vec![4]), 5);
        assert_eq!(slice_plus_slice(&vec![1, 2, 3], &vec![4, 5, 6]), 21);
        assert_eq!(slice_plus_slice(&vec![-1, -2, -3], &vec![-4, -5, -6]), -21);
    }
}
