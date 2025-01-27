fn remove_exclamation_marks(input: &str) -> String {
    input.split('!').collect()
}

#[cfg(test)]
mod tests {
    use super::remove_exclamation_marks;

    fn do_test(input: &str, expected: &str) {
        let actual = remove_exclamation_marks(input);
        assert_eq!(actual, expected, "\nYour result (left) did not match the expected output (right) for the input: {input:?}");
    }

    #[test]
    fn sample_test() {
        do_test("Hello World!", "Hello World");
        do_test("Hello World!!!", "Hello World");
        do_test("Hi! Hello!", "Hi Hello");
        do_test("", "");
        do_test("Oh, no!!!", "Oh, no");
    }
}
