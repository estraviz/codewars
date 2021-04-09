"""Invalid Login - Bug Fixing #11"""

from database import Database


def validate(username, password):
    return Database().login(username, password)
