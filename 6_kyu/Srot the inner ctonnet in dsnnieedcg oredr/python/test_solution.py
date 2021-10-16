import pytest

from solution import sort_the_inner_content


tests = [
    (
        "ww sort the inner content in descending order ss",
        "ww srot the inner ctonnet in dsnnieedcg oredr ss"
    ),
    (
        "wait for me",
        "wiat for me"
    ),
    (
        "this kata is easy",
        "tihs ktaa is esay"
    ),
    (
        "xkophgu ynszyuj gqvndtssgx srjsirrelx ykkchzu cxqpl ycwy cyjfjtwxto",
        "xpokhgu yzyusnj gvtssqngdx ssrrrljiex yzkkhcu cxqpl ywcy cyxwttjjfo"
    ),
    (
        "oyrakahzi a hxeqtq phn gwrxftvmk f k qfoz",
        "ozyrkhaai a hxtqeq phn gxwvtrmfk f k qofz"
    )
]


@pytest.mark.parametrize(
    "words, expected", tests
)
def test_sort_the_inner_content(words, expected):
    assert sort_the_inner_content(words) == expected
