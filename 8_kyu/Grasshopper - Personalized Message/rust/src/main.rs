fn greet(name: &str, owner: &str) -> String {
    let mut s = String::from("Hello ");
    let person: &str = match name == owner {
        true => "boss",
        _ => "guest",
    };
    s.push_str(person);
    s
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_greet() {
        assert_eq!(greet("Daniel", "Daniel"), "Hello boss");
        assert_eq!(greet("Greg", "Daniel"), "Hello guest");
    }
}
