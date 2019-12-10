from remove_url_anchor import remove_url_anchor


def test_remove_url_anchor():
    assert remove_url_anchor("www.codewars.com#about") == "www.codewars.com"
    assert remove_url_anchor("www.codewars.com/katas/?page=1#about"
                             ) == "www.codewars.com/katas/?page=1"
    assert remove_url_anchor(
        "www.codewars.com/katas/") == "www.codewars.com/katas/"
