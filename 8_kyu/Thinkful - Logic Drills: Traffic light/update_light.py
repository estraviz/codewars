"""
Thinkful - Logic Drills: Traffic light
"""


def update_light(current):
    return {"green": "yellow", "yellow": "red", "red": "green"}[current]
