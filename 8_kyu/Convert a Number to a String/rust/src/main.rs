fn number_to_string(i: i32) -> String {
    i.to_string()
}

#[cfg(test)]
mod tests {
    use super::number_to_string;

    fn dotest(n: i32, expected: &str) {
        let actual = number_to_string(n);
        assert!(
            actual == expected,
            "With n = {n}\nExpected \"{expected}\" but got \"{actual}\""
        )
    }

    #[test]
    fn fixed_tests() {
        dotest(67, "67");
        dotest(79585, "79585");
        dotest(1 + 2, "3");
        dotest(1 - 2, "-1");
    }
}
