const RENT_PER_DAY: u32 = 40;
const LONG_PERIOD_DAYS: u32 = 7;
const LONG_PERIOD_DISCOUNT: u32 = 50;
const SHORT_PERIOD_DAYS: u32 = 3;
const SHORT_PERIOD_DISCOUNT: u32 = 20;

fn rental_car_cost(num_days: u32) -> u32 {
    let mut cost: u32 = num_days * RENT_PER_DAY;

    if num_days >= LONG_PERIOD_DAYS {
        cost -= LONG_PERIOD_DISCOUNT;
    } else if num_days >= SHORT_PERIOD_DAYS {
        cost -= SHORT_PERIOD_DISCOUNT;
    }

    cost
}

#[cfg(test)]
mod tests {
    use super::rental_car_cost;

    fn dotest(d: u32, expected: u32) {
        let actual = rental_car_cost(d);
        assert_eq!(
            actual, expected,
            "You result: \"{}\" did not match the expected output: \"{}\"",
            actual, expected
        );
    }

    #[test]
    fn sample_tests() {
        dotest(1, 40);
        dotest(4, 140);
        dotest(7, 230);
        dotest(8, 270);
        dotest(0, 0);
    }
}
