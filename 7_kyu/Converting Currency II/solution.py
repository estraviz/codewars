"""
Converting Currency II
"""

currencies = {'USD': (0, '$', 1.1363636), 'EUR': (-1, '€', 1 / 1.1363636)}


def solution(to_cur, values):
    try:
        (position, symbol, multiplier) = currencies.get(to_cur)
    except Exception:
        return None
    return list(
        map(
            lambda amount:
            f'{symbol if position == 0 else ""}{round(amount * multiplier, 2):,.2f}{symbol if position == -1 else ""}',
            values))