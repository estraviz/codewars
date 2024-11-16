fn get_planet_name(id: u32) -> String {
    match id {
        1 => "Mercury".to_string(),
        2 => "Venus".to_string(),
        3 => "Earth".to_string(),
        4 => "Mars".to_string(),
        5 => "Jupiter".to_string(),
        6 => "Saturn".to_string(),
        7 => "Uranus".to_string(),
        8 => "Neptune".to_string(),
        _ => unreachable!(),
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_get_planet_name() {
        assert_eq!(get_planet_name(3), "Earth");
    }
}
