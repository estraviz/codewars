use std::collections::HashMap;

fn cannons_ready(gunners: HashMap<&str, &str>) -> String {
    if gunners.values().all(|x| *x == "aye") {
        String::from("Fire!")
    } else {
        String::from("Shiver me timbers!")
    }
}

#[cfg(test)]
mod tests {
    use super::cannons_ready;
    use std::collections::HashMap;

    #[test]
    fn test_should_fire_the_cannons_when_ready() {
        assert_eq!(
            cannons_ready(HashMap::from([
                ("Mike", "aye"),
                ("Joe", "aye"),
                ("Johnson", "aye"),
                ("Peter", "aye"),
            ])),
            "Fire!"
        );
    }

    #[test]
    fn test_should_shiver_your_timbers_instead_if_not_ready() {
        assert_eq!(
            cannons_ready(HashMap::from([
                ("Mike", "aye"),
                ("Joe", "nay"),
                ("Johnson", "aye"),
                ("Peter", "aye"),
            ])),
            "Shiver me timbers!"
        );
    }
}
