# Pell Numbers
import functools


class Pell(object):

    @functools.lru_cache(maxsize=1000)
    def get(self, n):
        if n < 2:
            return n
        else:
            return 2*self.get(n-1) + self.get(n-2)
