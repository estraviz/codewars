"""Duck Shoot - Easy Version"""

LIVE_DUCK = "2"
DEAD_DUCK = "X"


def duck_shoot(ammo, aim, ducks):
    successful_shots = int(ammo * aim)
    return ducks.replace(LIVE_DUCK, DEAD_DUCK, successful_shots)
