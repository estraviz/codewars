// Define a function "square" here which takes a signed integer of type i32
// and returns the square of that integer

#[allow(non_upper_case_globals)]
static square: fn(i32) -> i32 = |n| n.pow(2);

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn sample_tests() {
        assert_eq!(square(1), 1, "expected 1 squared to be 1");
        assert_eq!(square(2), 4, "expected 2 squared to be 4");
        assert_eq!(square(3), 9, "expected 3 squared to be 9");
        assert_eq!(square(4), 16, "expected 4 squared to be 16");
        assert_eq!(square(5), 25, "expected 5 squared to be 25");
    }
}
