fn are_you_playing_banjo(name: &str) -> String {
    match name.chars().nth(0).expect("").to_ascii_uppercase() {
        'R' => format!("{name} plays banjo"),
        _ => format!("{name} does not play banjo"),
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_are_you_playing_banjo() {
        assert_eq!(
            are_you_playing_banjo("Martin"),
            "Martin does not play banjo"
        );
        assert_eq!(are_you_playing_banjo("Rikke"), "Rikke plays banjo");
        assert_eq!(are_you_playing_banjo("bravo"), "bravo does not play banjo");
        assert_eq!(are_you_playing_banjo("rolf"), "rolf plays banjo");
    }
}
