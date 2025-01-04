M_PER_KM = 1000
CM_PER_M = 100
MIN_PER_HOUR = 60
SEG_PER_MIN = 60


def cockroach_speed(s):
    return int(s * M_PER_KM * CM_PER_M / (MIN_PER_HOUR * SEG_PER_MIN))
