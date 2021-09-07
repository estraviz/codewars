"""Find the calculation type"""


def calc_type(a, b, res):
    try:
        return {
            a + b: "addition",
            a - b: "subtraction",
            a * b: "multiplication",
            a / b: "division"
        }.get(res)
    except ZeroDivisionError:
        raise "Division by 0"
    except Exception:
        raise "No operation correspondence"
