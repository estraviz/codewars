fn pillars(num_of_pillars: u32, distance: u32, width: u32) -> u32 {
    match num_of_pillars > 1 {
        true => (num_of_pillars - 1) * distance * 100 + (num_of_pillars - 2) * width,
        _ => 0,
    }
}

#[cfg(test)]
mod tests {
    use super::pillars;

    #[test]
    fn sample_tests() {
        let cases = [((1, 10, 10), 0), ((2, 20, 25), 2000), ((11, 15, 30), 15270)];
        for ((p, d, w), expected) in cases {
            let actual = pillars(p, d, w);
            assert_eq!(actual, expected,
                "\nYour result (left) did not match expected output (right) for the inputs:\n pillars = {p}\ndistance = {d}\n   width = {w}"
            );
        }
    }
}
