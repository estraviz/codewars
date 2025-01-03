fn maps(values: &Vec<i32>) -> Vec<i32> {
    values.iter().map(|x| 2 * x).collect()
}

macro_rules! compare {
    ( $got : expr, $expect : expr ) => {
        if $got != $expect {
            panic!("Got: {:?}\nExpect: {:?}\n", $got, $expect);
        }
    };
}

#[test]
fn sample_tests() {
    compare!(maps(&vec![1, 2, 3, 4]), vec![2, 4, 6, 8]);
    compare!(maps(&vec![12, 5, 9, 7]), vec![24, 10, 18, 14]);
    compare!(
        maps(&vec![19037, 2793, 345, 544, 43]),
        vec![38074, 5586, 690, 1088, 86]
    );
    compare!(
        maps(&vec![-7, -43, -98, -45, -32, -1123, -1]),
        vec![-14, -86, -196, -90, -64, -2246, -2]
    );
    compare!(
        maps(&vec![7, -43, -98, 45, 32, 0, -1, 3]),
        vec![14, -86, -196, 90, 64, 0, -2, 6]
    );
    compare!(maps(&vec![]), vec![] as Vec<i32>);
}
