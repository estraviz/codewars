fn collinearity(x1: i32, y1: i32, x2: i32, y2: i32) -> bool {
    x1 * y2 == x2 * y1
}

#[cfg(test)]
mod tests {
    use super::*;

    fn do_test(x1: i32, y1: i32, x2: i32, y2: i32, expected: bool) {
        assert_eq!(
            collinearity(x1, y1, x2, y2),
            expected,
            "Input: ({x1}, {y1}, {x2}, {y2})"
        );
    }

    #[test]
    fn test_fixed_one_direction() {
        do_test(1, 1, 1, 1, true);
        do_test(1, 2, 2, 4, true);
        do_test(1, 2, 3, 7, false);
    }

    #[test]
    fn test_fixed_opposite_direction() {
        do_test(1, 1, 6, 1, false);
        do_test(1, 2, -1, -2, true);
        do_test(1, 2, 1, -2, false);
    }

    #[test]
    fn test_fixed_vectors_contain_zero() {
        do_test(4, 0, 11, 0, true);
        do_test(0, 1, 6, 0, false);
        do_test(4, 4, 0, 4, false);
    }

    #[test]
    fn test_fixed_vector_with_0_0_coordinates() {
        do_test(0, 0, 0, 0, true);
        do_test(0, 0, 1, 0, true);
        do_test(5, 7, 0, 0, true);
    }
}
