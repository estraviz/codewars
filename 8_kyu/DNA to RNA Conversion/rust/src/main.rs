fn dna_to_rna(dna: &str) -> String {
    dna.replace('T', "U")
}

#[cfg(test)]
mod tests {
    use super::dna_to_rna;

    #[test]
    fn returns_expected() {
        assert_eq!(dna_to_rna("TTTT"), "UUUU");
        assert_eq!(dna_to_rna("GCAT"), "GCAU");
    }
}
