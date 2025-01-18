fn count_positives_sum_negatives(input: Vec<i32>) -> Vec<i32> {
    if input.is_empty() {
        return Vec::new();
    }

    let mut positives: i32 = 0;
    let mut negatives: i32 = 0;

    for x in input.iter() {
        match x {
            x if x > &0 => positives += 1,
            x if x < &0 => negatives += x,
            _ => (),
        }
    }

    [positives, negatives].to_vec()
}

#[cfg(test)]
mod tests {
    use super::count_positives_sum_negatives;

    fn dotest(a: &[i32], expected: &[i32]) {
        let actual = count_positives_sum_negatives(a.to_vec());
        assert!(
            actual == expected,
            "With input = {a:?}\nExpected {expected:?} but got {actual:?}"
        )
    }
    #[test]
    fn fixed_tests() {
        dotest(
            &[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15],
            &[10, -65],
        );
        dotest(&[], &[]);
        dotest(
            &[0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14],
            &[8, -50],
        );
        dotest(&[0, 1, 2, 3, 4, 5], &[5, 0]);
        dotest(&[1, 2, 3, 4, 5], &[5, 0]);
        dotest(&[0, -1, -2, -3, -4, -5], &[0, -15]);
        dotest(&[-1, -2, -3, -4, -5], &[0, -15]);
        dotest(&[0, 0, 0, 0], &[0, 0]);
        dotest(&[0], &[0, 0]);
    }
}
