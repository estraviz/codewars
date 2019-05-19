from move_zeros import move_zeros


def test_only_numbers():
    a = [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]
    b = [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]
    assert move_zeros(a) == b

    a = [9, 0.0, 0, 9, 1, 2, 0, 1, 0, 1, 0.0, 3, 0, 1, 9, 0, 0, 0, 0, 9]
    b = [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert move_zeros(a) == b


def test_chars_and_numbers():
    a = ["a", 0, 0, "b", "c", "d", 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]
    b = ["a", "b", "c", "d", 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert move_zeros(a) == b


def test_includes_False_and_None():
    a = ["a", 0, 0, "b", None, "c", "d", 0, 1, False, 0, 1, 0, 3, [], 0, 1, 9,
         0, 0, {}, 0, 0, 9]
    b = ["a", "b", None, "c", "d", 1, False, 1, 3, [], 1, 9, {}, 9, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0]
    assert move_zeros(a) == b

    a = [0, 1, None, 2, False, 1, 0]
    b = [1, None, 2, False, 1, 0, 0]
    assert move_zeros(a) == b


def test_nothing_to_move():
    assert move_zeros(["a", "b"]) == ["a", "b"]
    assert move_zeros(["a"]) == ["a"]
    assert move_zeros([0, 0]) == [0, 0]
    assert move_zeros([0]) == [0]
    assert move_zeros([False]) == [False]
    assert move_zeros([]) == []
