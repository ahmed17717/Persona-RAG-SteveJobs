import requests
from bs4 import BeautifulSoup
import json
import os

def scrape_goodreads_quotes(pages=5):
    quotes = []
    base_url = "https://www.goodreads.com/author/quotes/5255891.Steve_Jobs?page="

    for page in range(1, pages+1):
        r = requests.get(base_url + str(page), headers={"User-Agent": "Mozilla/5.0"})
        if r.status_code != 200:
            continue

        soup = BeautifulSoup(r.text, "html.parser")
        for div in soup.find_all("div", class_="quoteText"):
            text = div.get_text(strip=True, separator=" ").split("―")[0].strip()
            if text:
                quotes.append(text)

    os.makedirs("data", exist_ok=True)
    with open("data/steve_jobs_quotes.json", "w", encoding="utf-8") as f:
        json.dump(quotes, f, indent=2, ensure_ascii=False)

    return quotes

if __name__ == "__main__":
    scrape_goodreads_quotes()
