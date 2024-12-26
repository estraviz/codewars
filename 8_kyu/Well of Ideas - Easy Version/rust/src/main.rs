fn well(x: &[&str]) -> &'static str {
    let count: usize = x.iter().filter(|&n| *n == "good").count();

    match count {
        0 => "Fail!",
        1 => "Publish!",
        2 => "Publish!",
        _ => "I smell a series!",
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_sample() {
        assert_eq!(well(&["bad", "bad", "bad"]), "Fail!");
        assert_eq!(well(&["good", "bad", "bad", "bad"]), "Publish!");
        assert_eq!(
            well(&["good", "bad", "bad", "bad", "bad", "good", "bad", "bad", "good"]),
            "I smell a series!"
        );
    }
}
