"""Custom Array Filters"""

class list:

    def __init__(self, arr):
        self.arr = arr

    def even(self):
        try:
            return [x for x in self.arr if type(x) == int and x % 2 == 0]
        except TypeError:
            return []

    def odd(self):
        return [x for x in self.arr if x % 2]

    def under(self, n):
        try:
            return [x for x in self.arr if x < n]
        except TypeError:
            return []

    def over(self, n):
        try:
            return [x for x in self.arr if x > n]
        except TypeError:
            return []

    def in_range(self, a, b):
        return [x for x in self.arr if x in range(a, b+1)]
