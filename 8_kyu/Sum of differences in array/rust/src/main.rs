fn sum_of_differences(arr: &[i8]) -> Option<i8> {
    if arr.len() <= 1 {
        return None;
    }

    let mut owned_arr = arr.to_owned();
    owned_arr.sort_by(|a, b| b.cmp(a));

    let result: i8 = owned_arr
        .iter()
        .zip(owned_arr.iter().skip(1))
        .map(|(&x, &y)| x - y)
        .collect::<Vec<_>>()
        .iter()
        .sum::<i8>();
    Some(result)
}

#[cfg(test)]
mod tests {
    use super::sum_of_differences;

    const ERR_MSG: &str = "\nYour result (left) did not match the expected output (right)";
    #[test]
    fn sample_tests() {
        assert_eq!(sum_of_differences(&[1, 2, 10]), Some(9), "{}", ERR_MSG);
        assert_eq!(sum_of_differences(&[-3, -2, -1]), Some(2), "{}", ERR_MSG);
        assert_eq!(sum_of_differences(&[1, 1, 1, 1, 1]), Some(0), "{}", ERR_MSG);
        assert_eq!(sum_of_differences(&[-17, 17]), Some(34), "{}", ERR_MSG);
        assert_eq!(sum_of_differences(&[]), None, "{}", ERR_MSG);
        assert_eq!(sum_of_differences(&[0]), None, "{}", ERR_MSG);
        assert_eq!(sum_of_differences(&[-1]), None, "{}", ERR_MSG);
        assert_eq!(sum_of_differences(&[1]), None, "{}", ERR_MSG);
    }
}
