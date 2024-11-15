use std::collections::HashMap;

fn greet(language: &str) -> &str {
    create_greetings()
        .get(&language)
        .unwrap_or_else(|| &"Welcome")
}

fn create_greetings() -> HashMap<&'static str, &'static str> {
    let mut greetings: HashMap<&str, &str> = HashMap::new();

    greetings.insert("english", "Welcome");
    greetings.insert("czech", "Vitejte");
    greetings.insert("danish", "Velkomst");
    greetings.insert("dutch", "Welkom");
    greetings.insert("estonian", "Tere tulemast");
    greetings.insert("finnish", "Tervetuloa");
    greetings.insert("flemish", "Welgekomen");
    greetings.insert("french", "Bienvenue");
    greetings.insert("german", "Willkommen");
    greetings.insert("irish", "Failte");
    greetings.insert("italian", "Benvenuto");
    greetings.insert("latvian", "Gaidits");
    greetings.insert("lithuanian", "Laukiamas");
    greetings.insert("polish", "Witamy");
    greetings.insert("spanish", "Bienvenido");
    greetings.insert("swedish", "Valkommen");
    greetings.insert("welsh", "Croeso");

    greetings
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_fixed() {
        assert_eq!(greet("english"), "Welcome");
        assert_eq!(greet("dutch"), "Welkom");
        assert_eq!(greet("IP_ADDRESS_INVALID"), "Welcome");
        assert_eq!(greet(""), "Welcome");
        assert_eq!(greet("swelsh"), "Welcome");
    }
}
