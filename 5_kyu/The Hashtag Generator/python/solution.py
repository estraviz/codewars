"""The Hashtag Generator"""


def generate_hashtag(s):
    return False if not s or len(s) > 140 \
                 else '#' + "".join(w.title() for w in s.split())
