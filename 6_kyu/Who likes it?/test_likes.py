from likes import likes


def test_likes():
    assert likes([]) == 'no one likes this'
    assert likes(['Peter']) == 'Peter likes this'
    assert likes(['Jacob', 'Alex']) == 'Jacob and Alex like this'
    assert likes(['Max', 'John', 'Mark']) == 'Max, John and Mark like this'

    message = 'Alex, Jacob and 2 others like this'
    assert likes(['Alex', 'Jacob', 'Mark', 'Max']) == message
