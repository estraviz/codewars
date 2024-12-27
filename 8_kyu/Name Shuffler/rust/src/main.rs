fn name_shuffler(s: &str) -> String {
    let name_parts: Vec<&str> = s.split_whitespace().collect();

    vec![name_parts[1], name_parts[0]].join(" ")
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_basic() {
        assert_eq!(name_shuffler("john McClane"), "McClane john");
        assert_eq!(name_shuffler("Mary jeggins"), "jeggins Mary");
        assert_eq!(name_shuffler("tom jerry"), "jerry tom");
    }
}
