fn is_divisible(n: i32, x: i32, y: i32) -> bool {
    n % x == 0 && n % y == 0
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn basic_tests() {
        assert_eq!(is_divisible(3, 3, 4), false);
        assert_eq!(is_divisible(12, 3, 4), true);
        assert_eq!(is_divisible(8, 3, 4), false);
        assert_eq!(is_divisible(48, 3, 4), true);
        assert_eq!(is_divisible(100, 5, 10), true);
        assert_eq!(is_divisible(100, 5, 3), false);
        assert_eq!(is_divisible(4, 4, 2), true);
        assert_eq!(is_divisible(5, 2, 3), false);
        assert_eq!(is_divisible(17, 17, 17), true);
        assert_eq!(is_divisible(17, 1, 17), true);
    }
}