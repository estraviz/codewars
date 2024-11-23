fn goals(la_liga_goals: i32, champions_league_goals: i32, copa_del_rey_goals: i32) -> i32 {
    la_liga_goals + champions_league_goals + copa_del_rey_goals
}

#[cfg(test)]
mod tests {
    use super::goals;

    fn dotest(a: i32, b: i32, c: i32, expected: i32) {
        let actual = goals(a, b, c);
        assert!(actual == expected,
             "With la_liga_goals = {a}, champions_league_goals = {b}, copa_del_rey_goals = {c}\nExpected {expected} but got {actual}")
    }

    #[test]
    fn test_goals() {
        dotest(0, 0, 0, 0);
        dotest(43, 10, 5, 58);
    }
}
