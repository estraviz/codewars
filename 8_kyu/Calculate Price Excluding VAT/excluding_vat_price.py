'''Calculate Price Excluding VAT
'''
VAT = .15


def excluding_vat_price(price):
    return -1 if price is None else round(price/(1+VAT), 2)
