"""
Simple Fun #74: Growing Plant
"""


def growing_plant(up_speed, down_speed, desired_height):
    num_day, actual_height = 0, 0
    while True:
        num_day += 1
        actual_height += up_speed
        if actual_height >= desired_height:
            return num_day
        else:
            actual_height -= down_speed
