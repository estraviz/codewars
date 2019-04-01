from likes import likes


def test_no_name():
    assert likes([]) == 'no one likes this'


def test_one_name():
    assert likes(['Peter']) == 'Peter likes this'


def test_two_names():
    assert likes(['Jacob', 'Alex']) == 'Jacob and Alex like this'


def test_three_names():
    assert likes(['Max', 'John', 'Mark']) == 'Max, John and Mark like this'


def test_four_or_more_names():
    message = 'Alex, Jacob and 2 others like this'
    assert likes(['Alex', 'Jacob', 'Mark', 'Max']) == message
