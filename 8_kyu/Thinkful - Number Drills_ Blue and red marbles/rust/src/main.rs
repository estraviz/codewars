fn guess_blue(blue_start: u32, red_start: u32, blue_pulled: u32, red_pulled: u32) -> f32 {
    let num_blue_marbles = (blue_start - blue_pulled) as f32;
    let num_red_marbles = (red_start - red_pulled) as f32;

    let num_total_marbles = num_blue_marbles + num_red_marbles;
    let prob_blue_marble = num_blue_marbles / num_total_marbles;

    prob_blue_marble
}

#[test]
fn basic_tests() {
    assert_eq!(guess_blue(5, 5, 2, 3), 0.6);
    assert_eq!(guess_blue(5, 7, 4, 3), 0.2);
    assert_eq!(guess_blue(12, 18, 4, 6), 0.4);
}
