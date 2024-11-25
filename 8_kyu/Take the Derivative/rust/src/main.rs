fn derive(coefficient: u32, exponent: u32) -> String {
    let base: u32 = coefficient * exponent;
    let exponent: u32 = exponent - 1;
    format!("{}x^{}", base.to_string(), &exponent.to_string())
}

#[cfg(test)]
mod tests {
    use super::derive;

    #[test]
    fn test_basics() {
        assert_eq!(derive(7, 8), "56x^7");
        assert_eq!(derive(5, 9), "45x^8");
    }
}
