fn points(games: &[String]) -> u32 {
    games
        .iter()
        .map(|game| {
            let Some((home, away)) = game.split_once(":") else {
                return 0;
            };
            game_points(home, away)
        })
        .sum()
}

fn game_points(home: &str, away: &str) -> u32 {
    match home.cmp(&away) {
        std::cmp::Ordering::Greater => 3,
        std::cmp::Ordering::Equal => 1,
        std::cmp::Ordering::Less => 0,
    }
}

#[cfg(test)]
mod tests {
    use super::points;

    const ERR_MSG: &str = "\nYour result (left) did not match the expected output (right)";

    fn do_fixed_test(e: &[&str], expected: u32) {
        let a = &e.iter().map(|x| x.to_string()).collect::<Vec<_>>();
        assert_eq!(points(a), expected, "{ERR_MSG} with games = {a:?}")
    }

    #[test]
    fn fixed_tests() {
        do_fixed_test(
            &[
                "1:0", "2:0", "3:0", "4:0", "2:1", "3:1", "4:1", "3:2", "4:2", "4:3",
            ],
            30,
        );
        do_fixed_test(
            &[
                "1:1", "2:2", "3:3", "4:4", "2:2", "3:3", "4:4", "3:3", "4:4", "4:4",
            ],
            10,
        );
        do_fixed_test(
            &[
                "0:1", "0:2", "0:3", "0:4", "1:2", "1:3", "1:4", "2:3", "2:4", "3:4",
            ],
            0,
        );
        do_fixed_test(
            &[
                "1:0", "2:0", "3:0", "4:0", "2:1", "1:3", "1:4", "2:3", "2:4", "3:4",
            ],
            15,
        );
        do_fixed_test(
            &[
                "1:0", "2:0", "3:0", "4:4", "2:2", "3:3", "1:4", "2:3", "2:4", "3:4",
            ],
            12,
        );
    }
}
