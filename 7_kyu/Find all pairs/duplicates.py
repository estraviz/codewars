"""
Find all pairs
"""


def duplicates(arr):
    dic = {}
    for num in arr:
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1
    return sum(value // 2 for value in dic.values() if value > 1)
