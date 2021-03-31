"""How far will I go?"""


def travel(total_time, run_time, rest_time, speed):
    distance = 0
    while total_time > 0:
        if total_time < run_time:
            run_time = total_time
        distance += run_time * speed
        total_time -= (run_time + rest_time)
    return distance
