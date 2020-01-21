from calculate_total import calculate_total


def test_calculate_total():
    tests = [
        # [(subtotal, tax, tip), total]
        [(5.00, 5, 10), 5.75],
        [(36.97, 7, 15), 45.10],
        [(0.00, 6, 18), 0.00],
        [(80.94, 0, 20), 97.13],
        [(54.96, 8, 0), 59.36],
    ]

    for inp, exp in tests:
        assert (calculate_total(*inp)) == exp
