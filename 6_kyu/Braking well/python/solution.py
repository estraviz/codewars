"""Braking well"""

from math import sqrt

REACTION_TIME = 1
G = 9.81


def dist(v, mu):                    	# suppose reaction time is 1
    return v * 1000 / 3600 * REACTION_TIME + (v * 1000 / 3600)**2 / (2 * mu * G)


def speed(d, mu):           			# suppose reaction time is 1
    return (-1 * REACTION_TIME + sqrt(REACTION_TIME**2 + 2 * d / (mu * G))) * (mu * G) * 3600 / 1000
