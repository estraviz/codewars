fn make_negative(n: i32) -> i32 {
    -n.abs()
}

#[cfg(test)]
mod tests {
    use super::make_negative;

    #[test]
    fn sample_tests() {
        assert_eq!(make_negative(1), -1);
        assert_eq!(make_negative(-5), -5);
        assert_eq!(make_negative(0), 0);
    }
}
