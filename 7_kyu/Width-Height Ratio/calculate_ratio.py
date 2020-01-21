"""
Width-Height Ratio
"""

from fractions import Fraction


def calculate_ratio(w, h):
    if w == 0 or h == 0:
        return "You threw an error"
    if w / h == w // h:
        return f'{w//h}:1'
    return {
        1024 / 768: '4:3',
        1920 / 1080: '16:9',
        600 / 800: '3:4',
        600 / 600: '1:1'
    }.get(w / h, f'{Fraction(w, h)}'.replace('/', ':'))
