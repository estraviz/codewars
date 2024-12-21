fn symmetric_point(p: [i32; 2], q: [i32; 2]) -> [i32; 2] {
    [2 * q[0] - p[0], 2 * q[1] - p[1]]
}

mod tests {
    use super::symmetric_point;
    fn dotest(p: [i32; 2], q: [i32; 2], exp: [i32; 2]) {
        let actual = symmetric_point(p, q);
        assert!(
            actual == exp,
            "With p = {p:?} and q = {q:?}\nExpected {exp:?} but got {actual:?}"
        )
    }

    #[test]
    fn test() {
        dotest([0, 0], [1, 1], [2, 2]);
        dotest([2, 6], [-2, -6], [-6, -18]);
        dotest([10, -10], [-10, 10], [-30, 30]);
        dotest([1, -35], [-12, 1], [-25, 37]);
        dotest([1000, 15], [-7, -214], [-1014, -443]);
        dotest([0, 0], [0, 0], [0, 0]);
    }
}
