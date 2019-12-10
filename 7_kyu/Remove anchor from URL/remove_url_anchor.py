"""
Remove anchor from URL
"""


def remove_url_anchor(url):
    return url.split('#')[0]
