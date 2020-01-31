from random_case import random_case


def test_random_case():
    v = [
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
        "Donec eleifend cursus lobortis", "THIS IS AN ALL CAPS STRING",
        "These guidelines are designed to be compatible with Joe Celko’s SQL Programming Style book",
        "much harder with a physical book.",
        "This guide is a little more opinionated in some areas and in others a little more relaxed",
        "—such as unnecessary quoting or parentheses or WHERE clauses that can otherwise be derived.",
        "Object oriented design principles should not be applied to SQL or database structures.",
        "collective name or, less ideally, a plural form. For example (in order of preference) staff and employees",
        "THIS IS AN ALL CAPS STRING",
        "this is an all lower string"
    ]

    for i in v:
        r = random_case(i)
        assert r.lower() == i.lower()
        assert r != i
        assert r != i.upper()
        assert r != i.lower()
