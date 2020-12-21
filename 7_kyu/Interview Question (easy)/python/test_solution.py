import pytest

from solution import get_strings


@pytest.mark.parametrize(
    "city, solution",
    [
        ("Chicago", "c:**,h:*,i:*,a:*,g:*,o:*"),
        ("Bangkok", "b:*,a:*,n:*,g:*,k:**,o:*"),
        ("Las Vegas", "l:*,a:**,s:**,v:*,e:*,g:*"),
        (
            "Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch",
            "l:***********,a:***,n:****,f:*,i:***,r:****,p:*,w:****,g:*******,y:*****,o:******,e:*,c:**,h:**,d:*,b:*,t:*,s:*",
        ),
    ],
)
def test_get_strings(city, solution):
    assert get_strings(city) == solution
