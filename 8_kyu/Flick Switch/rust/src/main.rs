fn flick_switch(list: &[&str]) -> Vec<bool> {
    let mut v = Vec::<bool>::new();
    let mut flag: bool = true;

    for s in list {
        if *s == "flick" {
            flag = !flag;
        }
        v.push(flag);
    }
    v
}

#[cfg(test)]
mod tests {
    use std::borrow::Borrow;

    use super::flick_switch;

    fn test_flick<'a, S: Borrow<[&'a str]>, E: Borrow<[bool]>>(strings: S, expected: E) {
        let strings: &[&'a str] = strings.borrow();
        let expected: &[bool] = expected.borrow();
        assert_eq!(flick_switch(strings), expected);
    }

    #[test]
    fn fixed_tests() {
        test_flick(
            ["codewars", "flick", "code", "wars"],
            [true, false, false, false],
        );
        test_flick(
            ["flick", "11037", "3.14", "53"],
            [false, false, false, false],
        );
        test_flick(
            ["false", "false", "flick", "sheep", "flick"],
            [true, true, false, false, true],
        );
        test_flick(["bicycle"], [true]);
        test_flick(["john, smith, susan", "flick"], [true, false]);
        test_flick(
            ["flick", "flick", "flick", "flick", "flick"],
            [false, true, false, true, false],
        );
        test_flick([], []);
    }
}
