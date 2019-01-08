from bmi import bmi


def test_bmi():
    assert bmi(50, 1.80) == "Underweight"
    assert bmi(80, 1.80) == "Normal"
    assert bmi(90, 1.80) == "Overweight"
    assert bmi(110, 1.80) == "Obese"
    assert bmi(50, 1.50) == "Normal"
