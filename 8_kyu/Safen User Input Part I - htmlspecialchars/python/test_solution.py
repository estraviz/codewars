import pytest

from solution import html_special_chars


tests = [
    ("<h2>Hello World</h2>", "&lt;h2&gt;Hello World&lt;/h2&gt;"),
    ("Hello, how would you & I fare?", "Hello, how would you &amp; I fare?"),
    ('How was "The Matrix"?  Did you like it?', 'How was &quot;The Matrix&quot;?  Did you like it?'),
    ("<script>alert('Website Hacked!');</script>", "&lt;script&gt;alert('Website Hacked!');&lt;/script&gt;"),
]


@pytest.mark.parametrize(
    "data, expected", tests
)
def test_html_special_chars(data, expected):
    assert html_special_chars(data) == expected
