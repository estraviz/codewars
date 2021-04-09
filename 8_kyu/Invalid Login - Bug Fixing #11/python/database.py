

class Database():

    user_list = [
        {'username': 'Timmy', 'password': 'password'},
        {'username': 'Johny', 'password': 'Hf7FAbf6'},
        {'username': 'Alice', 'password': 'alice'},
        {'username': 'Roger', 'password': 'pass'},
        {'username': 'Simon', 'password': 'says'},
        {'username': 'Admin', 'password': 'ads78adsg7dasga'}
    ]

    def login(cls, u, p):
        for item in cls.user_list:
            if item['username'] == u and item['password'] == p:
                return 'Successfully Logged in!'
        return 'Wrong username or password!'
