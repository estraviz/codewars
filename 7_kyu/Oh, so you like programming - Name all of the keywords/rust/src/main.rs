use std::collections::HashSet;

/* only 39 strict keywords counts, no reserved like abstract or override - as of 2021 Edition */
fn keywords() -> HashSet<&'static str> {
    HashSet::from([
        "as", "async", "await", "break", "const", "continue", "crate", "dyn", "else", "enum",
        "extern", "false", "fn", "for", "if", "impl", "in", "let", "loop", "match", "mod", "move",
        "mut", "pub", "ref", "return", "Self", "self", "static", "struct", "super", "trait",
        "true", "type", "unsafe", "use", "where", "while",
    ])
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_count() {
        assert_eq!(keywords().len(), 38, "there should be 38 keywords!");
    }
}
