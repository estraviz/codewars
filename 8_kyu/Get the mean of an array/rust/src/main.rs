fn get_average(marks: &[i32]) -> i32 {
    marks.iter().sum::<i32>() / marks.len() as i32
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_get_average() {
        assert_eq!(get_average(&[2, 2, 2, 2]), 2);
        assert_eq!(get_average(&[1, 5, 87, 45, 8, 8]), 25);
        assert_eq!(get_average(&[2, 5, 13, 20, 16, 16, 10]), 11);
        assert_eq!(
            get_average(&[1, 2, 15, 15, 17, 11, 12, 17, 17, 14, 13, 15, 6, 11, 8, 7]),
            11
        );
    }
}
