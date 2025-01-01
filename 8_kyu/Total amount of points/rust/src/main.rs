fn points(games: &[String]) -> u32 {
    let mut points: u32 = 0;

    let mut result: Vec<&str>;
    let mut home: u32;
    let mut away: u32;

    for game in games.iter() {
        result = game.split(":").collect();
        home = to_u32(result[0]);
        away = to_u32(result[1]);

        points += match home > away {
            true => 3,
            _ => match home < away {
                true => 0,
                _ => 1,
            },
        }
    }

    points
}

fn to_u32(x: &str) -> u32 {
    x.parse::<u32>().unwrap()
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
