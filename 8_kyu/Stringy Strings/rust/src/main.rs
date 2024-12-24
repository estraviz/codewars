fn stringy(size: usize) -> String {
    let mut output: String = String::new();

    for i in 0..size {
        let digits: String = ((i + 1) % 2).to_string();
        output += &digits;
    }

    output
}

#[cfg(test)]
mod tests {
    use super::stringy;

    fn dotest(n: usize, expected: &str) {
        let actual = stringy(n);
        assert!(
            actual == expected,
            "With size = {n}\nExpected \"{expected}\" but got \"{actual}\""
        )
    }

    #[test]
    fn should_start_with_one() {
        let actual = stringy(10);
        assert!(
            actual.chars().next() == Some('1'),
            "Whoops your string doesn't start with a '1'"
        )
    }

    #[test]
    fn should_have_the_correct_length() {
        for n in 1..5 {
            assert!(stringy(n).len() == n, "stringy({n}).len() != {n}")
        }
    }

    #[test]
    fn fixed_tests() {
        dotest(3, "101");
        dotest(5, "10101");
        dotest(12, "101010101010");
        dotest(26, "10101010101010101010101010");
        dotest(28, "1010101010101010101010101010");
    }
}
