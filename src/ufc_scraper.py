import requests
from bs4 import BeautifulSoup

def scrape_event(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    status_div = soup.find("div", class_="c-hero__headline-suptitle")
    status = status_div.text.strip() if status_div else "Status niet gevonden"

    card_segments = []
    for segment in soup.find_all("div", class_="c-card-event--time-location"):
        time = segment.find("div", class_="c-card-event--time")
        if time:
            card_segments.append(time.text.strip())

    fights = []
    for fight in soup.find_all("div", class_="c-card-fight--content"):
        names = fight.find_all("h3", class_="c-card-fight__title")
        for name in names:
            fights.append(name.text.strip())

    return {
        "status": status,
        "start_times": card_segments,
        "fights": fights
    }
