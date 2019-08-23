"""
Get Zodiac Sign
"""

import pandas as pd


def get_zodiac_sign(day, month):
    df = load_df()
    index = df.index[(df['date_min'] <= f"{month:02}{day:02}")
                     & (f"{month:02}{day:02}" <= df['date_max'])]
    if index.notnull():
        return index
    else:
        return 'Capricorn'


def load_df():
    df = pd.DataFrame(
        {
            'month_min':
            [f'{x:02}'
             for x in range(3, 13)] + [f'{x:02}' for x in range(1, 3)],
            'day_min': [
                '21', '20', '21', '21', '23', '23', '23', '23', '22', '22',
                '20', '19'
            ],
            'month_max':
            [f'{x:02}'
             for x in range(4, 13)] + [f'{x:02}' for x in range(1, 4)],
            'day_max': [
                '19', '20', '20', '22', '22', '22', '22', '21', '21', '19',
                '18', '20'
            ]
        },
        columns=['month_min', 'day_min', 'month_max', 'day_max'],
        index=[
            'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra',
            'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'
        ])
    df['date_min'] = df['month_min'] + df['day_min']
    df['date_max'] = df['month_max'] + df['day_max']
    return df
