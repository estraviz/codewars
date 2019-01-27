"""Classic Hello World
"""


class HelloWorld:
    def __init__(self):
        pass

    @staticmethod
    def main(*args):
        if args:
            return f"Hello World {', '.join(arg for arg in args)}!"
        return f'Hello World!'
