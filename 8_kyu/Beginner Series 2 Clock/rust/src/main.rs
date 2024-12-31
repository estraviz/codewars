fn past(h: i32, m: i32, s: i32) -> i32 {
    ((h * 60 + m) * 60 + s) * 1000
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn basic_tests() {
        assert_eq!(past(0, 1, 1), 61000);
        assert_eq!(past(1, 1, 1), 3661000);
        assert_eq!(past(0, 0, 0), 0);
        assert_eq!(past(1, 0, 1), 3601000);
        assert_eq!(past(1, 0, 0), 3600000);
    }
}
