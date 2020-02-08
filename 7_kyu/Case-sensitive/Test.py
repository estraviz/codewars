class Test:
    def __init__(self):
        pass

    @staticmethod
    def describe(message):
        print(message)

    @staticmethod
    def it(message):
        print(message)

    @staticmethod
    def assert_equals(actual, expected):
        if actual == expected:
            print("\tTest Passed!")
        else:
            print("\tTest Failed:")
            print(f"\t'{actual}' should equal '{expected}'")
