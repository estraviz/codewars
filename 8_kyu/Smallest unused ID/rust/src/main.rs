fn next_id(ids: &[usize]) -> usize {
    let iter = (0..ids.len()).skip_while(|x| ids.contains(&x)).next();

    if iter.is_none() {
        ids.len()
    } else {
        iter.unwrap()
    }
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
