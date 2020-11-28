"""
Even or Odd - Which is Greater?
"""


def even_or_odd(s):
    return {
        "even": "Even is greater than Odd",
        "odd": "Odd is greater than Even",
        "equal": "Even and Odd are the same",
    }.get(compare_sums(s))


def compare_sums(s):
    s_even = sum(int(x) for x in list(s) if int(x) % 2 == 0)
    s_odd = sum(int(x) for x in list(s) if int(x) % 2)
    return "even" if s_even > s_odd else "odd" if s_odd > s_even else "equal"
