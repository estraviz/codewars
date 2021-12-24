# Bits Battle
def bits_battle(numbers):
    odds, evens = 0, 0
    for x in numbers:
        for c in bin(x)[2:]:
            if x % 2 != 0 and c == '1':
                odds += 1
            elif x % 2 == 0 and c == '0':
                evens += 1
    return 'odds win' if odds > evens \
        else 'evens win' if odds < evens \
        else 'tie'
