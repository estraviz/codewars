from parse_float import parse_float


def test_parse_float():
    ts = (
        ("1.0", 1.0),
        ("a", None),
        ("234.0234", 234.0234)
    )

    for t in ts:
        assert parse_float(t[0]) == t[1]
