fn generate_range(min: usize, max: usize, step: usize) -> Vec<usize> {
    (min..=max).step_by(step).collect()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_basic_cases() {
        assert_eq!(generate_range(2, 10, 2), [2, 4, 6, 8, 10]);
        assert_eq!(generate_range(1, 10, 3), [1, 4, 7, 10]);
        assert_eq!(generate_range(1, 10, 1), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
        assert_eq!(generate_range(1, 10, 4), [1, 5, 9]);
        assert_eq!(generate_range(1, 10, 5), [1, 6]);
    }
}
