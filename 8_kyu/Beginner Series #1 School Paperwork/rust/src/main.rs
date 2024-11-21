fn paperwork(n: i16, m: i16) -> u32 {
    match (n, m) {
        (n, m) if (n < 0) || (m < 0) => 0,
        _ => (n * m) as u32,
    }
}

#[cfg(test)]
mod tests {
    use super::paperwork;

    fn dotest(n: i16, m: i16, expected: u32) {
        let actual = paperwork(n, m);
        assert!(
            actual == expected,
            "With n = {n}, m = {m}\nExpected {expected} but got {actual}"
        )
    }

    #[test]
    fn test_paperwork() {
        dotest(5, 5, 25);
        dotest(5, -5, 0);
        dotest(-5, -5, 0);
        dotest(-5, 5, 0);
        dotest(5, 0, 0);
    }
}
