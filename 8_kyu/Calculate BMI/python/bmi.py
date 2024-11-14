"""Calculate BMI
"""


def bmi(weight, height):
    coef = weight/height**2

    if coef <= 18.5:
        return "Underweight"
    elif coef <= 25.0:
        return "Normal"
    elif coef <= 30.0:
        return "Overweight"
    else:
        return "Obese"
