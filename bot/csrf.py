import requests
from bs4 import BeautifulSoup

from bot.constants import HOME_URL


def get_csrf():
    res = requests.get(HOME_URL)
    soup = BeautifulSoup(res.text, "html.parser")

    return soup.find('input', attrs={"name": "csrf-key"}).get("value")
