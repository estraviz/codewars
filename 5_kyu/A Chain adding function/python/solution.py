# A Chain adding function
class Add(int):

    def __call__(self, k):
        return Add(self + k)


def add(n):
    return Add(n)
