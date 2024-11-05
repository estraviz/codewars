pub fn is_leap_year(year: i32) -> bool {
    let mut is_leap: bool = false;

    if year % 4 == 0 {
        is_leap = true;

        if year % 100 == 0 {
            is_leap = false;

            if year % 400 == 0 {
                is_leap = true;
            }
        }
    }
    return is_leap;
}

#[cfg(test)]
mod sample_tests {
    use super::is_leap_year;

    fn do_test(year: i32, expected: bool) {
        let actual = is_leap_year(year);
        assert_eq!(
            actual, expected,
            "\nYour result (left) does not match the expected output (right) for the year {year:?}"
        );
    }

    #[test]
    fn year_2020_is_a_leap_year() {
        do_test(2020, true);
    }

    #[test]
    fn year_2000_is_a_leap_year() {
        do_test(2000, true);
    }

    #[test]
    fn year_2015_is_not_a_leap_year() {
        do_test(2015, false);
    }

    #[test]
    fn year_2100_is_not_a_leap_year() {
        do_test(2100, false);
    }
}
