import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
import os

os.makedirs('output', exist_ok=True)

HEADERS = {'User-Agent': 'Mozilla/5.0'}


def get_painting_urls():
    sitemap_url = 'https://www.nationalgallery.org.uk/xml-sitemap'

    response = requests.get(sitemap_url, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'xml')

    urls = []
    all_urls = soup.find_all('loc')
    for loc in all_urls:
        link = loc.get_text()
        if '/paintings/' in link:
            urls.append(link)

    return urls


def extract_painting_details(url):
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')

    details = {
        'Title': '',
        'Artist': 'N/A',
        'Artist dates': 'N/A',
        'Date made': 'N/A',
        'Inventory number': 'N/A',
        'Location': 'N/A',
        'url': url
    }

    title_element = soup.find('div', {'class': 'short-title'})
    if title_element:
        details['Title'] = title_element.get_text(strip=True)

    for dt in soup.find_all('dt'):
        label = dt.get_text(strip=True)
        dd = dt.find_next_sibling('dd')

        if label == 'Artist' and dd and dd.find('a'):
            details['Artist'] = dd.find('a').get_text(strip=True)

        elif label == 'Artist dates' and dd:
            details['Artist dates'] = dd.get_text(strip=True)

        elif label == 'Date made' and dd:
            details['Date made'] = dd.get_text(strip=True)

        elif label == 'Inventory number' and dd:
            details['Inventory number'] = dd.get_text(strip=True)

        elif label == 'Location' and dd and dd.find('a'):
            details['Location'] = dd.find('a').get_text(strip=True)

    return details


def main():
    painting_urls = get_painting_urls()
    painting_urls = painting_urls[:10]

    all_data = []
    for i, url in enumerate(painting_urls):
        print(f"[{i+1}/{len(painting_urls)}] Scraping: {url}")
        data = extract_painting_details(url)
        all_data.append(data)
        time.sleep(1)

    # save data to Excel
    df = pd.DataFrame(all_data)
    df.to_excel("output/paintings_data.xlsx", index=False)
    print("Data saved to paintings_data.xlsx")


if __name__ == "__main__":
    main()
