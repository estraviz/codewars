import pytest
from solution import doubles


@pytest.mark.parametrize(
    "s, result",
    [
        ["abbbzz", "ab"],
        ["zzzzykkkd", "ykd"],
        ["abbcccdddda", "aca"],
        ["vvvvvoiiiiin", "voin"],
        ["rrrmooomqqqqj", "rmomj"],
        ["xxbnnnnnyaaaaam", "bnyam"],
    ],
)
def test_doubles_basic(s, result):
    assert doubles(s) == result


@pytest.mark.parametrize(
    "s, result",
    [
        ["qqqqqqnpppgooooonpppppqmmmmmc", "npgonpqmc"],
        ["qqqqqwwwx", "qwx"],
        ["jjjfzzzzzzsddgrrrrru", "jfsgru"],
        ["jjjjjfuuuutgggggqppdaaas", "jftgqdas"],
        ["iiiiibllllllyqqqqqbiiiiiituuf", "ibyqbtf"],
        ["mmmmmmuzzqllllmqqqp", "uqmqp"],
    ],
)
def test_doubles_more_tests(s, result):
    assert doubles(s) == result
