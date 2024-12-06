fn close_compare(a: f64, b: f64, margin: f64) -> i8 {
    if margin >= (a - b).abs() {
        0
    } else if a < b {
        -1
    } else {
        1
    }
}

#[cfg(test)]
mod tests {
    use super::close_compare;

    const ERR_MSG: &str = "\nYour result (left) did not match the expected output (right)";

    fn dotest(a: f64, b: f64, margin: f64, expected: i8) {
        assert_eq!(
            close_compare(a, b, margin),
            expected,
            "{ERR_MSG} with a = {a}, b = {b}, margin = {margin}"
        )
    }

    #[test]
    fn fixed_tests() {
        dotest(4.0, 5.0, 0.0, -1);
        dotest(5.0, 5.0, 0.0, 0);
        dotest(6.0, 5.0, 0.0, 1);
        dotest(2.0, 5.0, 3.0, 0);
        dotest(5.0, 5.0, 3.0, 0);
        dotest(8.0, 5.0, 3.0, 0);
        dotest(8.1, 5.0, 3.0, 1);
        dotest(1.99, 5.0, 3.0, -1);
    }
}
