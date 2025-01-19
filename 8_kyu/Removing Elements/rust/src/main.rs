fn remove_every_other(arr: &[u8]) -> Vec<u8> {
    arr.into_iter().step_by(2).map(|&x| x).collect()
}

#[cfg(test)]
mod tests {
    use super::remove_every_other;

    #[test]
    fn sample_test() {
        assert_eq!(
            remove_every_other(&[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
            &[1, 3, 5, 7, 9]
        );
    }
}
