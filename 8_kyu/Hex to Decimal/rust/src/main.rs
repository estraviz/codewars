fn hex_to_dec(hex_string: &str) -> u32 {
    u32::from_str_radix(hex_string, 16).unwrap()
}

#[cfg(test)]
mod tests {
    use super::hex_to_dec;

    fn dotest(s: &str, expected: u32) {
        let actual = hex_to_dec(s);
        assert!(
            actual == expected,
            "With hex_string =\"{s}\"\nExpected {expected} but got {actual}"
        )
    }

    #[test]
    fn fixed_tests() {
        dotest("1", 1);
        dotest("a", 10);
        dotest("10", 16);
    }
}
