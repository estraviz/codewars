"""
Holiday VI - Shark Pontoon
"""


def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    if dolphin:
        shark_speed /= 2
    you_time = pontoon_distance / you_speed
    shark_time = shark_distance / shark_speed
    return "Alive!" if you_time < shark_time else "Shark Bait!"
