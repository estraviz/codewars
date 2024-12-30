fn feast(beast: &str, dish: &str) -> bool {
    let dish_start: char = dish.chars().next().unwrap();
    let dish_end: char = dish.chars().last().unwrap();

    beast.starts_with(dish_start) && beast.ends_with(dish_end)
}

#[test]
fn sample_test_cases() {
    assert_eq!(feast("great blue heron", "garlic naan"), true);
    assert_eq!(feast("chickadee", "chocolate cake"), true);
    assert_eq!(feast("brown bear", "bear claw"), false);
}
