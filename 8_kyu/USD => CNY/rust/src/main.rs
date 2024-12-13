fn usdcny(usd: u16) -> String {
    let cny: f64 = ((usd as f64) * 6.75 * 100.0).round() / 100.0;
    format!("{:.2}", cny) + " Chinese Yuan"
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_basic() {
        assert_eq!(usdcny(15), "101.25 Chinese Yuan");
        assert_eq!(usdcny(465), "3138.75 Chinese Yuan");
    }
}
