import random
from odd_count import odd_count


def test_odd_count():
    assert odd_count(15) == 7
    assert odd_count(15023) == 7511

    for i in range(0, 200):
        r = random.randrange(0, 9876543210)
        expected = odd_count(r)
        assert odd_count(r) == expected
        print(f'Test OK for n = {r}')
