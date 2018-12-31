from check_exam import check_exam


def test_check_exam():
    assert check_exam(["a", "a", "b", "b"], ["a", "c", "b", "d"]) == 6
    assert check_exam(["a", "a", "c", "b"], ["a", "a", "b",  ""]) == 7
    assert check_exam(["a", "a", "b", "c"], ["a", "a", "b", "c"]) == 16
    assert check_exam(["b", "c", "b", "a"], ["",  "a", "a", "c"]) == 0
