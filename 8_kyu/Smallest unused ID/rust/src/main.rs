fn next_id(ids: &[usize]) -> usize {
    (0..=ids.len())
        .find(|x| !ids.contains(x))
        .unwrap_or(ids.len())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_basics() {
        assert_eq!(next_id(&[0, 1, 2, 4, 5]), 3);
        assert_eq!(next_id(&[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 11);
    }
}
