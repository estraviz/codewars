from integrate import integrate


def test_integrate():
    assert integrate(3, 2) == "1x^3"
    assert integrate(12, 5) == "2x^6"
    assert integrate(20, 1) == "10x^2"
    assert integrate(40, 3) == "10x^4"
    assert integrate(90, 2) == "30x^3"
