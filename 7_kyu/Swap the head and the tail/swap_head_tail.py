"""
Swap the head and the tail
"""


def swap_head_tail(arr):
    if len(arr) % 2 == 0:
        return arr[len(arr)//2:len(arr)] + arr[0:len(arr)//2]
    else:
        return arr[len(arr)//2 + 1:len(arr)] + [arr[len(arr)//2]] + \
               arr[0:len(arr)//2]
