fn bonus_time(salary: u64, bonus: bool) -> String {
    let amount: u64 = match bonus {
        true => 10 * salary,
        _ => salary,
    };
    format!("¥{amount}")
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_basic_cases() {
        assert_eq!(bonus_time(10000, true), "¥100000");
        assert_eq!(bonus_time(25000, true), "¥250000");
        assert_eq!(bonus_time(10000, false), "¥10000");
        assert_eq!(bonus_time(60000, false), "¥60000");
        assert_eq!(bonus_time(2, true), "¥20");
        assert_eq!(bonus_time(78, false), "¥78");
        assert_eq!(bonus_time(67890, true), "¥678900");
    }
}
