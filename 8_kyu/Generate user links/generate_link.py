"""Generate user links
"""
from urllib.parse import quote


def generate_link(user):
    url = 'http://www.codewars.com/users/'
    return "{}{}".format(url, quote(user.encode('utf-8')))
