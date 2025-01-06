fn monkey_count(n: i32) -> Vec<i32> {
    (1..=n).collect()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test() {
        assert_eq!(monkey_count(5), vec![1, 2, 3, 4, 5]);
        assert_eq!(monkey_count(1), vec![1]);
        assert_eq!(monkey_count(0), vec![]);
        assert_eq!(
            monkey_count(12),
            vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        );
    }
}
