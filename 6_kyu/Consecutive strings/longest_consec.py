"""Consecutive strings
"""


def longest_consec(arr, k):
    if len(arr) == 0 or k > len(arr) or k <= 0:
        return ""
    return max(["".join(arr[i:i+k]) for i in range(0, len(arr)-k+1)], key=len)
