'''
Transportation on vacation
'''


def rental_car_cost(num_days):
    rent_per_day = 40
    long_period_days = 7
    long_period_discount = 50
    short_period_days = 3
    short_period_discount = 20

    cost = rent_per_day * num_days

    if num_days >= long_period_days:
        cost -= long_period_discount
    elif num_days >= short_period_days:
        cost -= short_period_discount

    return cost
