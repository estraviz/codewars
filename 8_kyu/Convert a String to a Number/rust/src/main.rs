fn string_to_number(s: &str) -> i32 {
    s.parse::<i32>().unwrap()
}

#[cfg(test)]
mod tests {
    use super::string_to_number;
    use rand::prelude::*;

    #[test]
    fn returns_expected() {
        assert_eq!(string_to_number("1234"), 1234);
        assert_eq!(string_to_number("605"), 605);
        assert_eq!(string_to_number("1405"), 1405);
        assert_eq!(string_to_number("-7"), -7);
    }

    #[test]
    fn works_on_random() {
        let mut rng = rand::thread_rng();
        for _ in 0..5 {
            let num: i32 = rng.gen();
            let input = num.to_string();
            assert_eq!(string_to_number(&input), num);
        }
    }
}
