import pytest

from solution import string_hash


tests = [
    ("a", 64),
    ("ca", -820),
    ("Hi", 16),
    (" Yo - What's Good?! ", 460),
    ("int main(int argc, char *argv[]) { return 0; }", 188),
    (" Yo - What's Good?! ", 460),
    (" df af asd ", 744),
    ("global hash", 1120),
    ("section .text", 328),
    ("hash:", -1884),
    ("    xor eax, eax", 1080),
    ("    ret", 112),
    ("; -----> end of hash <-----", -7136),
    ("int hash(const char *str);", -9232),
    ("", 32),
    (" ", 96),
    ("  ", 32),
    ("   ", 224),
    ("    ", 32),
]


@pytest.mark.parametrize(
    "s, expected", tests
)
def test_string_hash(s, expected):
    assert string_hash(s) == expected
