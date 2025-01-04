const M_PER_KM: f64 = 1000_f64;
const CM_PER_M: f64 = 100_f64;
const MIN_PER_HOUR: f64 = 60_f64;
const SEG_PER_MIN: f64 = 60_f64;

fn cockroach_speed(s: f64) -> i64 {
    (s * M_PER_KM * CM_PER_M / (MIN_PER_HOUR * SEG_PER_MIN)) as i64
}

#[cfg(test)]
mod sample_tests {
    use super::cockroach_speed;

    #[test]
    fn basic_tests() {
        test(1.08, 30);
        test(1.09, 30);
        test(0.0, 0);
    }

    fn test(speed: f64, expected: i64) {
        let actual = cockroach_speed(speed);
        assert_eq!(
            actual, expected,
            "\nYour result (left) did not match the expected result (right) for the speed {speed}"
        );
    }
}
