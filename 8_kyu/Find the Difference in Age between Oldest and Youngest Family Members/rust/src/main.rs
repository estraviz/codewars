fn difference_in_ages(ages: &[u8]) -> (u8, u8, u8) {
    let youngest: u8 = min_value(ages);
    let oldest: u8 = max_value(ages);
    let difference: u8 = oldest - youngest;

    (youngest, oldest, difference)
}

fn min_value(ages: &[u8]) -> u8 {
    let min_value = ages.iter().min().unwrap();

    *min_value
}

fn max_value(ages: &[u8]) -> u8 {
    let max_value = ages.iter().max().unwrap();

    *max_value
}

#[cfg(test)]
mod tests {
    use super::*;

    fn dotest(ages: &[u8], exp: (u8, u8, u8)) -> () {
        assert_eq!(
            difference_in_ages(ages),
            exp,
            "The result is not expected for \"{:?}\"",
            ages
        );
    }
    #[test]
    fn basic_test_cases() {
        dotest(&[16, 22, 31, 44, 3, 38, 27, 41, 88], (3, 88, 85));
        dotest(&[5, 8, 72, 98, 41, 16, 55], (5, 98, 93));
        dotest(&[57, 99, 14, 32], (14, 99, 85));
        dotest(&[62, 0, 3, 77, 88, 102, 26, 44, 55], (0, 102, 102));
        dotest(&[2, 44, 34, 67, 88, 76, 31, 67], (2, 88, 86));
        dotest(&[46, 86, 33, 29, 87, 47, 28, 12, 1, 4, 78, 92], (1, 92, 91));
        dotest(&[66, 73, 88, 24, 36, 65, 5], (5, 88, 83));
        dotest(&[12, 76, 49, 37, 29, 17, 3, 65, 84, 38], (3, 84, 81));
        dotest(&[0, 110], (0, 110, 110));
        dotest(&[33, 33, 33], (33, 33, 0));
        dotest(&[0, 0, 0], (0, 0, 0));
    }
}
