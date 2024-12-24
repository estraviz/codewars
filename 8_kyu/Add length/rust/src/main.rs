fn add_length(s: &str) -> Vec<String> {
    s.split_whitespace()
        .map(|x| format!("{} {}", x, x.len()))
        .collect()
}

#[cfg(test)]
mod tests {
    use super::add_length;

    fn dotest(s: &str, expected: &[String]) {
        let actual = add_length(s);
        assert!(
            actual == expected,
            "With s = \"{s}\"\nExpected {expected:?} but got {actual:?}"
        )
    }

    #[test]
    fn fixed_tests() {
        dotest(
            "apple ban",
            &["apple 5", "ban 3"]
                .iter()
                .map(|x| x.to_string())
                .collect::<Vec<_>>(),
        );
        dotest(
            "you will win",
            &["you 3", "will 4", "win 3"]
                .iter()
                .map(|x| x.to_string())
                .collect::<Vec<_>>(),
        );
        dotest(
            "y",
            &["y 1"].iter().map(|x| x.to_string()).collect::<Vec<_>>(),
        );
    }
}
