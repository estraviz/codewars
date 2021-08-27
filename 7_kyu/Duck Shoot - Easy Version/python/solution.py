"""Duck Shoot - Easy Version"""

LIVE_DUCK = "2"
DEAD_DUCK = "X"


def duck_shoot(ammo, aim, ducks):
    successful_shots = int(ammo * aim)
    result = list(ducks)
    for i, duck in enumerate(ducks):
        if successful_shots <= 0:
            break
        else:
            if duck == LIVE_DUCK:
                result[i] = DEAD_DUCK
                successful_shots -= 1
    return "".join(result)
