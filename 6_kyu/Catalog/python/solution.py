"""Catalog"""

from bs4 import BeautifulSoup


def catalog(s, article):
    catalog = load_catalog(s)
    output = ""
    for product in catalog:
        if article in product["name"]:
            name, prx, qty = product["name"], product["prx"], product["qty"]
            tmp = f"{name} > prx: ${prx} qty: {qty}"
            if output:
                output += "\r\n" + tmp
            else:
                output = tmp
    return output if output else "Nothing"


def load_catalog(s):
    soup = BeautifulSoup(s, "html.parser")
    catalog = []
    for products in soup.find_all("prod"):
        prod = {}
        for product in products:
            prod[product.name] = product.text
        catalog.append(prod)
    return catalog
