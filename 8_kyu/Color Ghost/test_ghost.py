from ghost import Ghost


def test_ghost():
    ghosts = []

    for i in range(1, 101):
        ghosts.append(Ghost().color)

    # it "should sometimes make white ghosts"
    assert ghosts.count("white") >= 1

    # it "should sometimes make yellow ghosts"
    assert ghosts.count("yellow") >= 1

    # it "should sometimes make purple ghosts"
    assert ghosts.count("purple") >= 1

    # it "should sometimes make red ghosts"
    assert ghosts.count("red") >= 1
