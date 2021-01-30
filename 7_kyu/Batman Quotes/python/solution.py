"""Batman Quotes"""

import re


class BatmanQuotes(object):
    @staticmethod
    def get_quote(quotes, hero):
        heroes = {"R": "Robin", "B": "Batman", "J": "Joker"}
        index = int(re.findall(r"\d", hero)[0])
        return f"{heroes.get(hero[0])}: {quotes[index]}"
