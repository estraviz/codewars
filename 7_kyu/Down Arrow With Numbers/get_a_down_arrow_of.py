"""
Down Arrow With Numbers
"""


def get_a_down_arrow_of(n):
    output = []
    k = n
    while k > 0:
        left = ''.join(str(i)[-1] for i in range(1, k))
        middle = str(k)[-1]
        right = left[::-1]
        output.append(left + middle + right + '\n' + ' ' *
                      (n - k + 1)) if k > 1 else output.append(middle)
        k -= 1
    return ''.join(output)
