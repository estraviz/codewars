from reverse_alternate import reverse_alternate


def test_reverse_alternate():
    assert reverse_alternate("Did it work?") == "Did ti work?"
    assert reverse_alternate("I really hope it works this time..."
                             ) == "I yllaer hope ti works siht time..."
    assert reverse_alternate(
        "Reverse this string, please!") == "Reverse siht string, !esaelp"
    assert reverse_alternate("Have a beer") == "Have a beer"
    assert reverse_alternate("") == ""
