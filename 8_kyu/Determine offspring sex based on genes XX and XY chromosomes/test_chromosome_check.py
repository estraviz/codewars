from chromosome_check import chromosome_check


def test_cases():
    sperm = 'XY'
    result = 'Congratulations! You\'re going to have a son.'
    assert chromosome_check(sperm) == result

    sperm = 'XX'
    result = 'Congratulations! You\'re going to have a daughter.'
    assert chromosome_check(sperm) == result
