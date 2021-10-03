import pytest

from solution import string_letter_count


tests = [
    ("The quick brown fox jumps over the lazy dog.",
     "1a1b1c1d3e1f1g2h1i1j1k1l1m1n4o1p1q2r1s2t2u1v1w1x1y1z"),
    ("The time you enjoy wasting is not wasted time.",
     "2a1d5e1g1h4i1j2m3n3o3s6t1u2w2y"),
    ("./4592#{}()", ""),
    ("This%Sentence\"is$$being^tested.", "1b1c1d6e1g1h3i3n4s4t"),
    ("abccdefgdhijklmno_pqrsTuvwxYz",
     "1a1b2c2d1e1f1g1h1i1j1k1l1m1n1o1p1q1r1s1t1u1v1w1x1y1z"),
    ("", ""),
    (".", ""),
    ("y", "1y"),
]


@pytest.mark.parametrize(
    "s, expected", tests
)
def test_string_letter_count(s, expected):
    assert string_letter_count(s) == expected
