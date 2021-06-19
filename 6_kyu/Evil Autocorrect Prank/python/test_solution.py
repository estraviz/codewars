import pytest

from solution import autocorrect


simple_tests = [
    ("u", "your sister"),
    ("you", "your sister"),
    ("Youuuuu", "your sister"),
    ("youtube", "youtube"),
]


@pytest.mark.parametrize(
    "input, expected", simple_tests
)
def test_should_autocorrect_simple_tests(input, expected):
    assert autocorrect(input) == expected


normal_tests = [
    ("I miss you!", "I miss your sister!"),
    ("u want to go to the movies?", "your sister want to go to the movies?"),
    ("Can't wait to see youuuuu", "Can't wait to see your sister"),
    ("I want to film the bayou with you and put it on youtube",
     "I want to film the bayou with your sister and put it on youtube"),
    ("You should come over Friday night",
     "your sister should come over Friday night"),
    ("You should come over Friday night",
     "your sister should come over Friday night"),
    ("You u youville utube you youyouyou uuu raiyou united youuuu u you",
     "your sister your sister youville utube your sister youyouyou uuu raiyou united your sister your sister your sister"),
]


@pytest.mark.parametrize(
    "input, expected", normal_tests
)
def test_should_autocorrect_normal_tests(input, expected):
    assert autocorrect(input) == expected


more_autocorrection_tests = [
    ("You = best kisser", "your sister = best kisser"),
    ("i <3 u", "i <3 your sister"),
    ("Let's put you on youtube", "Let's put your sister on youtube"),
    ("my friend Alabinyou is conveniently named, and he wants to make a website called youwin with youuu",
     "my friend Alabinyou is conveniently named, and he wants to make a website called youwin with your sister"),
    ("You should be famous on youville",
     "your sister should be famous on youville"),
    ("Hope to see u there!", "Hope to see your sister there!"),
]


@pytest.mark.parametrize(
    "input, expected", more_autocorrection_tests
)
def test_should_more_autocorrection_tests(input, expected):
    assert autocorrect(input) == expected
