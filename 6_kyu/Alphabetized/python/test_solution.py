import pytest

from solution import alphabetized


tests = [
    ("", ""),
    (" ", ""),
    (" a", "a"),
    ("a ", "a"),
    (" a ", "a"),
    ("A b B a", "AabB"),
    (" a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z",
     "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"),
    ("!@$%^&*()_+=-`,", ""),
    ("The Holy Bible", "BbeehHilloTy"),
    ("CodeWars can't Load Today", "aaaaCcdddeLnooorstTWy"),
]


@pytest.mark.parametrize(
    "s, expected", tests
)
def test_alphabetized(s, expected):
    assert alphabetized(s) == expected
