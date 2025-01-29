fn solution(phrase: &str) -> String {
    phrase.chars().rev().collect::<String>()
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn sample_test() {
        assert_eq!(solution("world"), "dlrow");
    }
}
