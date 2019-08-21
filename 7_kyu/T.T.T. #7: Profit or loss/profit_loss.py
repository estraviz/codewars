"""
T.T.T. #7: Profit or loss
"""


def profit_loss(records):
    return round(
        sum(price - price / (1 + percentage / 100)
            for [price, percentage] in records), 2)
