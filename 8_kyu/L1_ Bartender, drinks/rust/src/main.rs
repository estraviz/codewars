use std::collections::HashMap;

fn get_drink_by_profession(param: &str) -> &'static str {
    let profession_drinks: HashMap<&'static str, &'static str> = get_profession_drinks();
    let capitalized_words: String = capitalize_words(param);

    profession_drinks
        .get(capitalized_words.as_str())
        .unwrap_or(&"Beer")
}

fn get_profession_drinks() -> HashMap<&'static str, &'static str> {
    let mut profession_drinks = HashMap::new();
    profession_drinks.insert("Jabroni", "Patron Tequila");
    profession_drinks.insert("School Counselor", "Anything with Alcohol");
    profession_drinks.insert("Programmer", "Hipster Craft Beer");
    profession_drinks.insert("Bike Gang Member", "Moonshine");
    profession_drinks.insert("Politician", "Your tax dollars");
    profession_drinks.insert("Rapper", "Cristal");

    profession_drinks
}

fn capitalize_words(param: &str) -> String {
    param
        .split(" ")
        .map(|x| capitalize(x))
        .collect::<Vec<_>>()
        .join(" ")
}

fn capitalize(param: &str) -> String {
    param[..1].to_uppercase() + &param[1..].to_lowercase()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_tests() {
        assert_eq!(
            get_drink_by_profession("jabrOni"),
            "Patron Tequila",
            "'Jabroni' should map to 'Patron Tequila'"
        );
        assert_eq!(
            get_drink_by_profession("scHOOl counselor"),
            "Anything with Alcohol",
            "'School Counselor' should map to 'Anything with Alcohol'"
        );
        assert_eq!(
            get_drink_by_profession("prOgramMer"),
            "Hipster Craft Beer",
            "'Programmer' should map to 'Hipster Craft Beer'"
        );
        assert_eq!(
            get_drink_by_profession("bike ganG member"),
            "Moonshine",
            "'Bike Gang Member' should map to 'Moonshine'"
        );
        assert_eq!(
            get_drink_by_profession("poLiTiCian"),
            "Your tax dollars",
            "'Politician' should map to 'Your tax dollars'"
        );
        assert_eq!(
            get_drink_by_profession("rapper"),
            "Cristal",
            "'Rapper' should map to 'Cristal'"
        );
        assert_eq!(
            get_drink_by_profession("pundit"),
            "Beer",
            "'Pundit' should map to 'Beer'"
        );
        assert_eq!(
            get_drink_by_profession("Pug"),
            "Beer",
            "'Pug' should map to 'Beer'"
        );
    }
}
