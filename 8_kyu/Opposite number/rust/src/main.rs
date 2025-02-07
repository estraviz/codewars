fn opposite(number: i32) -> i32 {
    -number
}

#[test]
fn returns_expected() {
    assert_eq!(opposite(1), -1);
    assert_eq!(opposite(-1), 1);
}
