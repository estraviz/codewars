"""Help the bookseller !"""


def stock_list(list_of_art, list_of_cat):
    totals = {letter: 0 for letter in list_of_cat}
    for book in list_of_art:
        code, amount = book.split()
        if code[0] in list_of_cat:
            totals[code[0]] += int(amount)
    return (
        ""
        if not list_of_art
        else " - ".join(f"({key} : {value})" for key, value in totals.items())
    )
