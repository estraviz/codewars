"""
L1: Bartender, drinks!
"""


def get_drink_by_profession(param):
    drink_by_profession = {
        "Jabroni": "Patron Tequila",
        "School Counselor":	"Anything with Alcohol",
        "Programmer": "Hipster Craft Beer",
        "Bike Gang Member": "Moonshine",
        "Politician": "Your tax dollars",
        "Rapper": "Cristal"
    }
    return drink_by_profession.get(param.title(), "Beer")
