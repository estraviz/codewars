"""Meeting
"""


def meeting(s):
    names = [name.split(":") for name in s.split(";")]
    sort_by_name = sorted(
        [(surname.upper(), name.upper()) for name, surname in names],
        key=lambda x: x[1],
        reverse=False,
    )
    sort_by_surname = sorted(sort_by_name, key=lambda y: y[0], reverse=False)
    return "".join(f"({surname}, {name})" for surname, name in sort_by_surname)
