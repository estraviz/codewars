fn _if<T, F1, F2>(cond: bool, mut then: F1, mut els: F2) -> T
where
    F1: FnMut() -> T,
    F2: FnMut() -> T,
{
    if cond {
        then()
    } else {
        els()
    }
}

#[test]
fn should_support_true() {
    assert_eq!(_if(true, || 1, || 2), 1);
}

#[test]
fn should_support_false() {
    assert_eq!(_if(false, || 1, || 2), 2);
}

#[test]
fn should_support_false_other_type() {
    assert_eq!(_if(false, || 'a', || 'b'), 'b');
    assert_eq!(_if(true, || "True", || "False"), "True");
}

#[test]
fn should_support_closures() {
    let mut true_was_set = false;
    let result = _if(true, || true_was_set = true, || panic!("Fail"));
    assert!(true_was_set);
    assert_eq!(result, ())
}
