from symmetric_point import symmetric_point


def test_symmetric_point():
    assert symmetric_point([0, 0], [1, 1]) == [2, 2]
    assert symmetric_point([2, 6], [-2, -6]) == [-6, -18]
    assert symmetric_point([10, -10], [-10, 10]) == [-30, 30]
    assert symmetric_point([1, -35], [-12, 1]) == [-25, 37]
    assert symmetric_point([1000, 15], [-7, -214]) == [-1014, -443]
    assert symmetric_point([0, 0], [0, 0]) == [0, 0]
