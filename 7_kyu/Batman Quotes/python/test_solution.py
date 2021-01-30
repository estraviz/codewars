from solution import BatmanQuotes


quotes = [
    "WHERE IS SHE?!",
    "Holy haberdashery, Batman!",
    "Let's put a smile on that faaaceee!",
]


def test_robin_said_it():
    assert (
        BatmanQuotes.get_quote(quotes, "Rob1n") == "Robin: Holy haberdashery, Batman!"
    )


def test_batman_said_it():
    assert BatmanQuotes.get_quote(quotes, "Batm0n") == "Batman: WHERE IS SHE?!"


def test_joker_said_it():
    assert (
        BatmanQuotes.get_quote(quotes, "Jok2r")
        == "Joker: Let's put a smile on that faaaceee!"
    )
