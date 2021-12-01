# Bumps in the Road
def bumps(road):
    return "Woohoo!" if sum(r == "n" for r in road) <= 15 else "Car Dead"
