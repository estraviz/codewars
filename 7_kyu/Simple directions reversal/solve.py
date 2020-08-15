"""
Simple directions reversal
"""


def solve(arr):
    dirs, streets = [], []
    for instruction in arr:
        dirs.append(instruction.split(' on ')[0])
        streets.append(instruction.split(' on ')[1])
    dirs = ['Begin'] + dirs[::-1][:-1]
    dirs = [{'Right': 'Left', 'Left': 'Right'}.get(dir, dir) for dir in dirs]
    streets = streets[::-1]
    return [' on '.join([dir, street]) for dir, street in zip(dirs, streets)]
