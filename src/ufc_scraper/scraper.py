import requests
from bs4 import BeautifulSoup

def scrape_event(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Failed to fetch the page")

    soup = BeautifulSoup(response.text, "html.parser")
    
    event = {}
    event['title'] = soup.find("h1").text.strip() if soup.find("h1") else "Unknown"
    
    status_element = soup.find("div", class_="c-hero__headline-suffix")
    if status_element:
        event['status'] = status_element.text.strip().lower()
    else:
        event['status'] = "unknown"

    fights = []
    fight_cards = soup.find_all("div", class_="c-card-event--athlete")
    for fight in fight_cards:
        names = fight.find_all("h3", class_="c-card-event--athlete-name")
        if len(names) == 2:
            fights.append({
                "fighter1": names[0].text.strip(),
                "fighter2": names[1].text.strip()
            })
    event['fights'] = fights

    return event
