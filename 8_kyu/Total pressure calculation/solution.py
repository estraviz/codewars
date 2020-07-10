"""
Total pressure calculation
"""

R = 0.082
C_to_F = 273.15


def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp):
    n = (given_mass1 / molar_mass1 + given_mass2 / molar_mass2)
    T = (temp + C_to_F)
    return n * R * T / volume
