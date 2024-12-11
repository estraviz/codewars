fn contamination(text: &str, character: &str) -> String {
    if text.is_empty() || character.is_empty() {
        String::from("")
    } else {
        (0..text.len()).map(|_| character).collect()
    }
}

#[cfg(test)]
mod tests {
    use super::contamination;

    fn dotest(a: &str, b: &str, expected: &str) {
        let actual = contamination(a, b);
        assert!(actual == expected, "With text = \"{a}\", character = \"{b}\"\nExpected \"{expected}\" but got \"{actual}\"")
    }

    #[test]
    fn fixed_tests() {
        dotest("abc", "z", "zzz");
        dotest("", "z", "");
        dotest("abc", "", "");
        dotest("_3ebzgh4", "&", "&&&&&&&&");
        dotest("//case", " ", "      ");
    }
}
