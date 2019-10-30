"""
Converting Currency II
"""


def solution(to_cur, values):
    currencies = {'USD': (0, '$', 1.1363636), 'EUR': (-1, '€', 1 / 1.1363636)}
    try:
        (pos, symbol, factor) = currencies.get(to_cur)
        return list(
            map(
                lambda value:
                f'{symbol if pos == 0 else ""}{round(value * factor, 2):,.2f}{symbol if pos == -1 else ""}',
                values))
    except KeyError:
        return None
