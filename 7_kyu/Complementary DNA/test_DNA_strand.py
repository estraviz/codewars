from DNA_strand import DNA_strand


def test_DNA_strand():
    assert DNA_strand("AAAA") == "TTTT"
    assert DNA_strand("ATTGC") == "TAACG"
    assert DNA_strand("GTAT") == "CATA"
    assert DNA_strand("AAGG") == "TTCC"
    assert DNA_strand("CGCG") == "GCGC"
    assert DNA_strand("ATTGC") == "TAACG"

    s1 = "GTATCGATCGATCGATCGATTATATTTTCGACGAGATTTA"
    s2 = "AATATATATATATACGAGAGAATACAGATAGACAGATTA"
    s3 = "CATAGCTAGCTAGCTAGCTAATATAAAAGCTGCTCTAAAT"
    s4 = "TTATATATATATATGCTCTCTTATGTCTATCTGTCTAAT"
    assert DNA_strand(s1.join(s2)) == s3.join(s4)
