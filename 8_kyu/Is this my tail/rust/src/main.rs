fn correct_tail(body: &str, tail: char) -> bool {
    body.ends_with(tail)
}

#[cfg(test)]
mod tests {
    use super::correct_tail;

    #[test]
    fn fixed_tests() {
        assert_eq!(correct_tail("Fox", 'x'), true);
        assert_eq!(correct_tail("Rhino", 'o'), true);
        assert_eq!(correct_tail("Meerkat", 't'), true);
        assert_eq!(correct_tail("Emu", 't'), false);
        assert_eq!(correct_tail("Badger", 's'), false);
        assert_eq!(correct_tail("Giraffe", 'd'), false);
    }
}
