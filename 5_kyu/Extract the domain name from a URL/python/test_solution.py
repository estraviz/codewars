import pytest

from solution import domain_name


data = [
    ("http://google.com", "google"),
    ("http://google.co.jp", "google"),
    ("www.xakep.ru", "xakep"),
    ("https://youtube.com", "youtube"),
    ("https://123.net", "123"),
    ("https://hyphen-site.org", "hyphen-site"),
    ("http://codewars.com", "codewars"),
    ("http://www.codewars.com/kata/", "codewars"),
    ("icann.org", "icann"),
]


@pytest.mark.parametrize("url, result", data)
def test_domain_name(url, result):
    assert domain_name(url) == result
