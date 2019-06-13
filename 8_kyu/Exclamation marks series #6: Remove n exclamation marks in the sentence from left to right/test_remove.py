from remove import remove


tests = [
    # [[input],  [expected]],
    [["Hi!", 1],  "Hi"],
    [["Hi!", 100],  "Hi"],
    [["Hi!!!", 1],  "Hi!!"],
    [["Hi!!!", 100],  "Hi"],
    [["!Hi", 1],  "Hi"],
    [["!Hi!", 1],  "Hi!"],
    [["!Hi!", 100],  "Hi"],
    [["!!!Hi !!hi!!! !hi", 1],  "!!Hi !!hi!!! !hi"],
    [["!!!Hi !!hi!!! !hi", 3],  "Hi !!hi!!! !hi"],
    [["!!!Hi !!hi!!! !hi", 5],  "Hi hi!!! !hi"],
    [["!!!Hi !!hi!!! !hi", 100],  "Hi hi hi"],
]


def test_remove():
    for inp, exp in tests:
        assert remove(*inp) == exp
