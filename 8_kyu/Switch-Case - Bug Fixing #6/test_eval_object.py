from eval_object import eval_object


def test_eval_object():
    assert eval_object({'a': 1, 'b': 1, 'operation': '+'}) == 2
    assert eval_object({'a': 1, 'b': 1, 'operation': '-'}) == 0
    assert eval_object({'a': 1, 'b': 1, 'operation': '/'}) == 1
    assert eval_object({'a': 1, 'b': 1, 'operation': '*'}) == 1
    assert eval_object({'a': 1, 'b': 1, 'operation': '%'}) == 0
    assert eval_object({'a': 1, 'b': 1, 'operation': '**'}) == 1
