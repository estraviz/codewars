"""Simple Substitution Cipher Helper"""


class Cipher(object):
    def __init__(self, map1, map2):
        self.map1 = map1
        self.map2 = map2

    def encode(self, s):
        return self.apply_mapping(self.map1, self.map2, s)

    def decode(self, s):
        return self.apply_mapping(self.map2, self.map1, s)

    @staticmethod
    def apply_mapping(mapX, mapY, s):
        return "".join(c if c not in mapY else mapY[mapX.index(c)] for c in s)
