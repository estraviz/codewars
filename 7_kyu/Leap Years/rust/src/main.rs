fn is_leap_year(year: i32) -> bool {
    match year {
        year if year % 400 == 0 => true,
        year if year % 100 == 0 => false,
        year if year % 4 == 0 => true,
        _ => false,
    }
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
