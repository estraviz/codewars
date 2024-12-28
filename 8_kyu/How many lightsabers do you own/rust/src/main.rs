fn how_many_lightsabers_do_you_own(name: &str) -> u8 {
    match name {
        "Zach" => 18,
        _ => 0,
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn returns_zero_for_an_empty_string() {
        assert_eq!(how_many_lightsabers_do_you_own(""), 0);
    }
    #[test]
    fn returns_0_for_other_people() {
        assert_eq!(how_many_lightsabers_do_you_own("Adam"), 0);
    }
    #[test]
    fn returns_18_for_zach() {
        assert_eq!(how_many_lightsabers_do_you_own("Zach"), 18);
    }
    #[test]
    fn returns_0_when_zach_is_lowercased() {
        assert_eq!(how_many_lightsabers_do_you_own("zach"), 0);
    }
}
