# Map over a list of lists
def grid_map(inp, op):
    return [list(map(op, lst)) for lst in inp]
