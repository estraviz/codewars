fn greet(input: &str) -> String {
    let msg: &str = match input {
        "Johnny" => "my love",
        _ => input,
    };
    format!("Hello, {}!", msg)
}

#[test]
fn greets_some_people_normally() {
    assert_eq!(greet("Jim"), "Hello, Jim!");
    assert_eq!(greet("Jane"), "Hello, Jane!");
    assert_eq!(greet("Simon"), "Hello, Simon!");
}

#[test]
fn greets_johnny_special() {
    assert_eq!(greet("Johnny"), "Hello, my love!");
}
