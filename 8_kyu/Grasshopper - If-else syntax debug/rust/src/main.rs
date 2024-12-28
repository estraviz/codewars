fn check_alive(health: i8) -> bool {
    health > 0
}

#[cfg(test)]
mod tests {
    use super::check_alive;

    fn dotest(h: i8, expected: bool) {
        let actual = check_alive(h);
        assert!(
            actual == expected,
            "With health = {h}\nExpected {expected} but got {actual}"
        )
    }

    #[test]
    fn basic_tests() {
        dotest(5, true);
        dotest(0, false);
        dotest(-5, false);
    }
}
