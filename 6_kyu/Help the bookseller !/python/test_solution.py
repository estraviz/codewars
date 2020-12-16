from solution import stock_list


def test_stock_list():
    list_of_art = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
    list_of_cat = ["A", "B"]
    assert stock_list(list_of_art, list_of_cat) == "(A : 200) - (B : 1140)"
