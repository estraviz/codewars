# Codewars Leaderboard
from bs4 import BeautifulSoup
import requests

LEADERBOARD_URL = 'https://www.codewars.com/users/leaderboard'


def get_leaderboard_honor():
    scores = []
    html_content = requests.get(LEADERBOARD_URL).text
    soup = BeautifulSoup(html_content, "html.parser")
    table = soup.find("div", attrs={"class": "leaderboard p-0"}).table

    for row in table.find_all("tr")[1:]:
        _, _, _, score = row
        scores.append(int(str(score.text).replace(',', '')))
    return scores
