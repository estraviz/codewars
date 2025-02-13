use std::collections::HashMap;

fn update_light(current: &str) -> String {
    let traffic_lights = HashMap::from([("green", "yellow"), ("yellow", "red"), ("red", "green")]);

    traffic_lights
        .get(current)
        .expect("Not a valid traffic light")
        .to_string()
}

#[test]
fn basic_test() {
    assert_eq!(update_light("green"), "yellow");
    assert_eq!(update_light("yellow"), "red");
    assert_eq!(update_light("red"), "green");
}
