from partlist import partlist


def test_partlist():
    assert partlist(["I", "wish", "I", "hadn't", "come"]) == \
        [("I", "wish I hadn't come"),
            ("I wish", "I hadn't come"),
            ("I wish I", "hadn't come"),
            ("I wish I hadn't", "come")]

    assert partlist(["cdIw", "tzIy", "xDu", "rThG"]) == \
        [("cdIw", "tzIy xDu rThG"),
            ("cdIw tzIy", "xDu rThG"),
            ("cdIw tzIy xDu", "rThG")]

    assert partlist(["vJQ", "anj", "mQDq", "sOZ"]) == \
        [("vJQ", "anj mQDq sOZ"),
            ("vJQ anj", "mQDq sOZ"),
            ("vJQ anj mQDq", "sOZ")]

    assert partlist(["mkC", "WoiP", "pCHh", "mkv"]) == \
        [("mkC", "WoiP pCHh mkv"),
            ("mkC WoiP", "pCHh mkv"),
            ("mkC WoiP pCHh", "mkv")]

    assert partlist(["vHW", "bPq", "pme", "jJr", "HGHV"]) == \
        [("vHW", "bPq pme jJr HGHV"),
            ("vHW bPq", "pme jJr HGHV"),
            ("vHW bPq pme", "jJr HGHV"),
            ("vHW bPq pme jJr", "HGHV")]

    assert partlist(["YZd", "ptUD", "IXr"]) == \
        [("YZd", "ptUD IXr"),
            ("YZd ptUD", "IXr")]

    assert partlist(["dOXj", "nMlK", "QGT", "LSt", "BHNR"]) == \
        [("dOXj", "nMlK QGT LSt BHNR"),
            ("dOXj nMlK", "QGT LSt BHNR"),
            ("dOXj nMlK QGT", "LSt BHNR"),
            ("dOXj nMlK QGT LSt", "BHNR")]

    assert partlist(["UQB", "aIfC", "eVB", "aCL", "bWoU"]) == \
        [("UQB", "aIfC eVB aCL bWoU"),
            ("UQB aIfC", "eVB aCL bWoU"),
            ("UQB aIfC eVB", "aCL bWoU"),
            ("UQB aIfC eVB aCL", "bWoU")]

    assert partlist(["Pimt", "qxEm", "enzX", "Luk", "Smi"]) == \
        [("Pimt", "qxEm enzX Luk Smi"),
            ("Pimt qxEm", "enzX Luk Smi"),
            ("Pimt qxEm enzX", "Luk Smi"),
            ("Pimt qxEm enzX Luk", "Smi")]

    assert partlist(["CyAg", "zzWg", "ZZuR", "wbpx", "mYr"]) == \
        [("CyAg", "zzWg ZZuR wbpx mYr"),
            ("CyAg zzWg", "ZZuR wbpx mYr"),
            ("CyAg zzWg ZZuR", "wbpx mYr"),
            ("CyAg zzWg ZZuR wbpx", "mYr")]

    assert partlist(["Epb", "yTcb", "njU"]) == \
        [("Epb", "yTcb njU"),
            ("Epb yTcb", "njU")]
