fn repeat_str(src: &str, count: usize) -> String {
    (*src.to_string().repeat(count)).to_string()
}

#[test]
fn example_tests() {
    assert_eq!(repeat_str("a", 4), "aaaa");
    assert_eq!(repeat_str("hello ", 3), "hello hello hello ");
    assert_eq!(repeat_str("abc", 2), "abcabc");
}
