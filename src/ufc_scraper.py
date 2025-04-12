import requests
from bs4 import BeautifulSoup

def scrape_event(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Request failed with status code {response.status_code}")

    soup = BeautifulSoup(response.text, 'html.parser')

    # Zoek de status, bijvoorbeeld "Final", "Upcoming", etc.
    status_element = soup.find('div', class_='c-hero__headline-suffix')
    status = status_element.get_text(strip=True) if status_element else "Status not found"

    return {
        "event_url": url,
        "status": status
    }