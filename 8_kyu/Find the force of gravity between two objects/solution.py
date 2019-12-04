"""
Find the force of gravity between two objects
"""

G = 6.67 * 1e-11
ft_to_m = 0.3048
lb_to_kg = 0.453592


def solution(arr_val, arr_unit):
    mass_1, mass_2, dist_12 = arr_val
    unit_mass_1, unit_mass_2, unit_distance_12 = arr_unit

    mass_1 = convert_to_kg(mass_1, unit_mass_1)
    mass_2 = convert_to_kg(mass_2, unit_mass_2)
    dist_12 = convert_to_m(dist_12, unit_distance_12)

    return G * mass_1 * mass_2 / dist_12**2


def convert_to_kg(mass, unit):
    return mass * {
        'kg': 1,
        'g': 1e-3,
        'mg': 1e-6,
        'μg': 1e-9,
        'lb': lb_to_kg
    }.get(unit)


def convert_to_m(dist, unit):
    return dist * {
        'm': 1,
        'cm': 1e-2,
        'mm': 1e-3,
        'μm': 1e-6,
        'ft': ft_to_m
    }.get(unit)
