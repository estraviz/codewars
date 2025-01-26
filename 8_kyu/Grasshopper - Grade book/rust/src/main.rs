fn get_grade(s1: u16, s2: u16, s3: u16) -> char {
    match (s1 + s2 + s3) / 3 {
        m if m >= 90 && m <= 100 => 'A',
        m if m >= 80 && m <= 90 => 'B',
        m if m >= 70 && m <= 80 => 'C',
        m if m >= 60 && m <= 70 => 'D',
        _ => 'F',
    }
}

#[cfg(test)]
mod tests {
    use super::get_grade;

    fn dotest(s1: u16, s2: u16, s3: u16, expected: char) {
        let actual = get_grade(s1, s2, s3);
        assert!(
            actual == expected,
            "With s1 = {s1}, s2 = {s2}, s = {s3}\nExpected '{expected}' but got '{actual}'"
        )
    }

    #[test]
    fn test_get_grade() {
        dotest(100, 100, 100, 'A');
        dotest(95, 90, 93, 'A');
        dotest(82, 85, 87, 'B');
        dotest(60, 82, 76, 'C');
        dotest(58, 62, 70, 'D');
        dotest(58, 59, 60, 'F');
        dotest(0, 0, 0, 'F');
    }
}
