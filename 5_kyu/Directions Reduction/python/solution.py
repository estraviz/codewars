"""Directions Reduction"""


def dir_reduc(arr):
    reduc = {("NORTH", "SOUTH"), ("SOUTH", "NORTH"), ("WEST", "EAST"), ("EAST", "WEST")}
    new_arr = []

    while True:
        for dir in arr:
            if not new_arr:
                new_arr.append(dir)
            else:
                if (new_arr[-1], dir) in reduc:
                    new_arr.pop(-1)
                else:
                    new_arr.append(dir)

        if len(new_arr) == len(arr):
            return arr
        else:
            arr = new_arr
            new_arr = []
