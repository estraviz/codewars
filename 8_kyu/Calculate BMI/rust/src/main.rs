fn bmi(weight: u32, height: f32) -> &'static str {
    assert!(height > 0.0, "the height argument can not be zero.");
    let bmi: f32 = (weight as f32) / f32::powi(height, 2);
    match bmi {
        x if x <= 18.5 => "Underweight",
        x if x <= 25.0 => "Normal",
        x if x <= 30.0 => "Overweight",
        _ => "Obese",
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn basic_tests() {
        assert_eq!(bmi(50, 1.80), "Underweight");
        assert_eq!(bmi(80, 1.80), "Normal");
        assert_eq!(bmi(90, 1.80), "Overweight");
        assert_eq!(bmi(110, 1.80), "Obese");
    }

    #[test]
    #[should_panic(expected = "the height argument can not be zero.")]
    fn should_panic() {
        bmi(90, 0.0);
    }
}
