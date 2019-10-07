from solve import solve


def test_solve():
    assert solve("codewarriors") == 2
    assert solve("suoidea") == 3
    assert solve("ultrarevolutionariees") == 3
    assert solve("strengthlessnesses") == 1
    assert solve("cuboideonavicuare") == 2
    assert solve("chrononhotonthuooaos") == 5
    assert solve("iiihoovaeaaaoougjyaw") == 8
