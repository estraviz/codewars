"""
Grasshopper - Debug
"""


def weather_info(fahrenheit):
    celsius = round(convert_to_celsius(fahrenheit), 2)
    print(celsius)
    if celsius > 0:
        return "{} is above freezing temperature".format(celsius)
    return "{} is freezing temperature".format(celsius)


def convert_to_celsius(fahrenheit):
    return 5.*(fahrenheit - 32)/9
