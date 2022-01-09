# Elevator Distance
def elevator_distance(array):
    return sum(abs(f2 - f1) for f1, f2 in zip(array, array[1:]))
