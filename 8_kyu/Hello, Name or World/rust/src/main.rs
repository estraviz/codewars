fn hello(name: &str) -> String {
    let message: &str = "Hello, World!";
    let capitalized_name = capitalize(name);

    if !name.is_empty() {
        str::replace(message, "World", &capitalized_name)
    } else {
        String::from(message)
    }
}

fn capitalize(name: &str) -> String {
    let name_lowercase = String::from(name).to_lowercase();

    match name_lowercase.chars().next() {
        Some(x) => x.to_uppercase().collect::<String>() + &name_lowercase.as_str()[1..],
        None => String::new(),
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_basic() {
        assert_eq!(hello("jOhN"), "Hello, John!");
        assert_eq!(hello("alice"), "Hello, Alice!");
        assert_eq!(hello(""), "Hello, World!");
    }
}
