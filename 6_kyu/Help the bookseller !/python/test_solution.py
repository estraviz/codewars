import pytest

from solution import stock_list


@pytest.mark.parametrize(
    "list_of_art, list_of_cat, result",
    [
        (
            ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"],
            ["A", "B"],
            "(A : 200) - (B : 1140)",
        ),
        (
            ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"],
            ["A", "B", "C", "D"],
            "(A : 0) - (B : 1290) - (C : 515) - (D : 600)",
        ),
        (
            ["CBART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"],
            ["A", "B", "C", "W"],
            "(A : 0) - (B : 114) - (C : 70) - (W : 0)",
        ),
        (
            ["ROXANNE 102", "RHODODE 123", "BKWRKAA 125", "BTSQZFG 239", "DRTYMKH 060"],
            ["B", "R", "D", "X"],
            "(B : 364) - (R : 225) - (D : 60) - (X : 0)",
        ),
        ([], ["B", "R", "D", "X"], ""),
        (
            ["ROXANNE 102", "RHODODE 123", "BKWRKAA 125", "BTSQZFG 239", "DRTYMKH 060"],
            [],
            "",
        ),
        (
            ["ROXANNE 102", "RHODODE 123", "BKWRKAA 125", "BTSQZFG 239", "DRTYMKH 060"],
            ["U", "V", "R"],
            "(U : 0) - (V : 0) - (R : 225)",
        ),
    ],
)
def test_stock_list(list_of_art, list_of_cat, result):
    assert stock_list(list_of_art, list_of_cat) == result
