from replace_exclamation import replace_exclamation


def test_replace_exclamation():
    assert replace_exclamation("Hi!") == "H!!"
    assert replace_exclamation("!Hi! Hi!") == "!H!! H!!"
    assert replace_exclamation("aeiou") == "!!!!!"
    assert replace_exclamation("ABCDE") == "!BCD!"
    assert replace_exclamation("aeiou") == "!!!!!"
    assert replace_exclamation("AEIOU") == "!!!!!"
    assert replace_exclamation("AeIoU") == "!!!!!"
    assert replace_exclamation("aEiOu") == "!!!!!"
    assert replace_exclamation("Enter Sandman") == "!nt!r S!ndm!n"
    assert replace_exclamation("Live And Let Die") == "L!v! !nd L!t D!!"
    assert replace_exclamation("Thunderstruck") == "Th!nd!rstr!ck"
