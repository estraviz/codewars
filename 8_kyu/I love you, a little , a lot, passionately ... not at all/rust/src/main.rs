use std::collections::HashMap;

fn how_much_i_love_you(nb_petals: u16) -> &'static str {
    let mut phrases = HashMap::new();
    phrases.insert(0, "I love you");
    phrases.insert(1, "a little");
    phrases.insert(2, "a lot");
    phrases.insert(3, "passionately");
    phrases.insert(4, "madly");
    phrases.insert(5, "not at all");

    let index: u16 = (nb_petals - 1) % 6;

    phrases.get(&index).unwrap()
}

#[cfg(test)]
mod tests {
    use super::how_much_i_love_you;

    #[test]
    fn fixed_tests() {
        assert_eq!(how_much_i_love_you(7), "I love you");
        assert_eq!(how_much_i_love_you(3), "a lot");
        assert_eq!(how_much_i_love_you(6), "not at all");
    }
}
