fn abbrev_name(name: &str) -> String {
    name.split_whitespace()
        .map(|x| x.chars().nth(0).unwrap().to_uppercase().to_string())
        .collect::<Vec<String>>()
        .join(".")
}

#[test]
fn sample_tests() {
    assert_eq!(abbrev_name("Sam Harris"), "S.H");
    assert_eq!(abbrev_name("Patrick Feenan"), "P.F");
    assert_eq!(abbrev_name("patrick feeney"), "P.F");
    assert_eq!(abbrev_name("Evan Cole"), "E.C");
    assert_eq!(abbrev_name("P Favuzzi"), "P.F");
    assert_eq!(abbrev_name("David Mendieta"), "D.M");
}
