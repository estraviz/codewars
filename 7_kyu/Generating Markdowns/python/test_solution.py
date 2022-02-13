import pytest

from solution import generate_markdowns


TESTS_LINKS = [
    (
        'hyperlink',
        'https://en.wikipedia.org/wiki/Hyperlink',
        '[hyperlink](https://en.wikipedia.org/wiki/Hyperlink)'
    ),
    (
        'Google Search',
        'https://www.google.com.au/?safe=active',
        '[Google Search](https://www.google.com.au/?safe=active)'
    ),
    (
        'Bing',
        'https://www.bing.com/',
        '[Bing](https://www.bing.com/)'
    ),
    (
        'Codewars Kata',
        'https://www.codewars.com/kata',
        '[Codewars Kata](https://www.codewars.com/kata)'
    ),
    (
        'Codewars Dashboard',
        'https://www.codewars.com/dashboard',
        '[Codewars Dashboard](https://www.codewars.com/dashboard)'
    ),
    (
        'Codewars Dashboard',
        'codewars/dashboard',
        '[Codewars Dashboard](codewars/dashboard)'
    ),
    (
        'Codewars on Github',
        'https://www.github/codewars',
        '[Codewars on Github](https://www.github/codewars)'
    ),
    (
        'Codewars Kumite',
        'https://www.codewars.com/kumite',
        '[Codewars Kumite](https://www.codewars.com/kumite)'
    ),
]

TEST_IMG = [
    (
        'this should be a picture',
        'https://github.com/codewars/gna.jpg',
        '![this should be a picture](https://github.com/codewars/gna.jpg)',
    ),
]

TEST_CODE = [
    ('''def generate_markdowns(markdown, text, url_or_language):
    # Your code here!
    pass''', 'python', "```python\ndef generate_markdowns(markdown, text, url_or_language):\n    # Your code here!\n    pass\n```"),
]


@pytest.mark.parametrize(
    "txt, url, exp", TESTS_LINKS
)
def test_link_markdowns(txt, url, exp):
    assert generate_markdowns('link', txt, url) == exp


@pytest.mark.parametrize(
    "txt, url, exp", TEST_IMG
)
def test_image_markdowns(txt, url, exp):
    assert generate_markdowns('img', txt, url) == exp


@pytest.mark.parametrize(
    "txt, url, exp", TEST_CODE
)
def test_codeblock_markdowns(txt, url, exp):
    assert generate_markdowns('code', txt, url) == exp
