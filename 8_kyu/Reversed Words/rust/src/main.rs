fn reverse_words(words: &str) -> String {
    words.split_whitespace().rev().collect::<Vec<_>>().join(" ")
}

#[cfg(test)]
mod tests {
    use super::reverse_words;
    #[test]
    fn returns_expected() {
        assert_eq!(reverse_words("hello world!"), "world! hello");
        assert_eq!(
            reverse_words("The greatest victory is that which requires no battle"),
            "battle no requires which that is victory greatest The"
        );
    }
}
