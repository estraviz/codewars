from odd_or_even import odd_or_even


def test_odd_or_even():
    odd_or_even([0, 1, 2]) == 'odd'
    odd_or_even([0, 1, 3]) == 'even'
    odd_or_even([1023, 1, 2]) == 'even'
