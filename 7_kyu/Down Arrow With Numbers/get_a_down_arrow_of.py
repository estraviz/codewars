"""
Down Arrow With Numbers
"""


def get_a_down_arrow_of(n):
    output = ""
    k = n
    while k > 0:
        s = ''.join(str(i)[-1] for i in range(1, k))
        output += str(k)[-1] if k == 1 else s + str(
            k)[-1] + s[::-1] + '\n' + ' ' * (n - k + 1)
        k -= 1
    return output
