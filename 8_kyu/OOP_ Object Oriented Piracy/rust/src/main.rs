struct Ship {
    draft: u32,
    crew: u32,
}

impl Ship {
    pub fn new(draft: u32, crew: u32) -> Ship {
        Ship { draft, crew }
    }

    pub fn is_worth_it(&self) -> bool {
        (self.draft as f32) - 1.5 * (self.crew as f32) > (20 as f32)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    const ERR_MSG: &str = "\nYour result (left) did not match the expected output (right)";

    fn dotest(draft: u32, crew: u32, expected: bool) {
        let ship = Ship {
            draft: draft,
            crew: crew,
        };
        assert_eq!(
            ship.is_worth_it(),
            expected,
            "{ERR_MSG} with draft = {draft}, crew = {crew}"
        )
    }

    #[test]
    fn fixed_tests() {
        dotest(0, 0, false);
        dotest(15, 20, false);
        dotest(35, 20, false);
        dotest(100, 20, true);
        dotest(29, 6, false);
        dotest(30, 6, true);
    }
}
