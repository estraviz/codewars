"""longest_palindrome"""


def longest_palindrome(s):
    max_len = 0
    for i in range(len(s)):
        for j in range(len(s), i, -1):
            if max_len >= j - i:
                break
            else:
                sub_s = s[i:j]
                if is_palindrome(sub_s):
                    max_len = len(sub_s)
                    break
    return max_len


def is_palindrome(s):
    return s == s[::-1]
