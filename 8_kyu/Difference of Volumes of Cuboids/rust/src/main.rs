fn find_difference(a: &[i32; 3], b: &[i32; 3]) -> i32 {
    (a.iter().product::<i32>() - b.iter().product::<i32>()).abs()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn basic() {
        assert_eq!(find_difference(&[3, 2, 5], &[1, 4, 4]), 14);
        assert_eq!(find_difference(&[9, 7, 2], &[5, 2, 2]), 106);
        assert_eq!(find_difference(&[11, 2, 5], &[1, 10, 8]), 30);
        assert_eq!(find_difference(&[4, 4, 7], &[3, 9, 3]), 31);
        assert_eq!(find_difference(&[15, 20, 25], &[10, 30, 25]), 0);
    }
}
