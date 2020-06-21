"""
Thinkful - Dictionary drills: Order filler
"""


def fillable(stock, merch, n):
    return stock.get(merch, 0) >= n
