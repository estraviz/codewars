import pytest

from solution import clean_string


tests = [
    ('abc#d##c', "ac"),
    ('abc####d##c#', ""),
    ("#######", ""),
    ("", ""),
    ('abjd####jfk#', "jf"),
    ('gfh#jds###d#dsd####dasdaskhj###dhkjs####df##s##d##', "gdasda"),
    ('831####jns###s#cas/*####-5##s##6+yqw87e##hfklsd-=-28##fds##', "6+yqw8hfklsd-=-f"),
    ('######831###dhkj####jd#dsfsdnjkf###d####dasns', "jdsfdasns"),
    ('', ""),
    ('#######', ""),
    ('####gfdsgf##hhs#dg####fjhsd###dbs########afns#######sdanfl##db#####s#a', "sa"),
    ('#hskjdf#gd', "hskjdgd"),
    ('hsk48hjjdfgd', "hsk48hjjdfgd"),
]


@pytest.mark.parametrize(
    "s, expected", tests
)
def test_should_consider_backspace_char(s, expected):
    assert clean_string(s) == expected
