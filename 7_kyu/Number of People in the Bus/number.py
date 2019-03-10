"""Number of People in the Bus
"""


def number(bus_stops):
    return sum(people[0] - people[1] for people in bus_stops)
