fn to_csv_text(array: &[Vec<i8>]) -> String {
    let mut output = String::new();

    for vec in array {
        for (i, digit) in &mut vec.iter().enumerate() {
            output += digit.to_string().as_str();

            if i == vec.len() - 1 {
                output += "\n";
            } else {
                output += ",";
            }
        }
    }

    output[..output.len() - 1].to_string()
}

#[cfg(test)]
mod tests {
    use super::to_csv_text;

    fn do_test(input: &[Vec<i8>], expected: &str) {
        let actual = to_csv_text(input);
        assert!(
            actual == expected,
            "Test failed with array = {input:?}\nExpected \"{expected}\"\nbut got \"{actual}\""
        );
    }

    #[test]
    fn fixed_tests() {
        for (input, expected) in [
            (
                vec![
                    vec![0, 1, 2, 3, 45],
                    vec![10, 11, 12, 13, 14],
                    vec![20, 21, 22, 23, 24],
                    vec![30, 31, 32, 33, 34],
                ],
                "0,1,2,3,45\n10,11,12,13,14\n20,21,22,23,24\n30,31,32,33,34",
            ),
            (
                vec![vec![-25, 21, 2, -33, 48], vec![30, 31, -32, 33, -34]],
                "-25,21,2,-33,48\n30,31,-32,33,-34",
            ),
            (
                vec![
                    vec![5, 55, 5, 5, 55],
                    vec![6, 6, 66, 23, 24],
                    vec![127, 31, 66, 33, 7],
                ],
                "5,55,5,5,55\n6,6,66,23,24\n127,31,66,33,7",
            ),
        ] {
            do_test(&input, expected)
        }
    }
}
