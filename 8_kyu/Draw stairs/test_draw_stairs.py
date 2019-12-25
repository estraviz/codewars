from draw_stairs import draw_stairs


def test_draw_stairs():
    stairs = '''I\n I\n  I'''
    assert draw_stairs(3) == stairs

    stairs = '''I\n I\n  I\n   I\n    I'''
    assert draw_stairs(5) == stairs
