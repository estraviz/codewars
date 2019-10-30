"""
Converting Currency II
"""


def solution(to_cur, values):
    eur_to_usd = 1.1363636

    if to_cur == 'USD':
        return [f'${round(value * eur_to_usd, 2):,.2f}' for value in values]

    if to_cur == 'EUR':
        return [f'{round(value / eur_to_usd, 2):,.2f}€' for value in values]
