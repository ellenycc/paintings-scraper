import requests
from bs4 import BeautifulSoup
from typing import Dict
from ngscraper.sitemap import HEADERS
from ngscraper.thumbnail import get_thumbnail_url


def extract_painting_details(painting_url: str) -> Dict:
    """
    Extract painting details i.e. title, artist, artist dates, 
    date made, inventory number, location and url from each painting's url.

    Args:
        painting_url (str): url of a painting

    Returns:
        Dict: Dictionary of painting details
    """
    try:
        response = requests.get(painting_url, headers=HEADERS)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching {painting_url}: {e}")
        return {
            'Title': '',
            'Artist': 'N/A',
            'Artist dates': 'N/A',
            'Date made': 'N/A',
            'Inventory number': 'N/A',
            'Location': 'N/A',
            'Painting URL': painting_url,
            'Thumbnail URL': 'N/A'
        }

    soup = BeautifulSoup(response.content, 'html.parser')

    details = {
        'Title': '',
        'Artist': 'N/A',
        'Artist dates': 'N/A',
        'Date made': 'N/A',
        'Inventory number': 'N/A',
        'Location': 'N/A',
        'Painting URL': painting_url,
        'Thumbnail URL': 'N/A'
    }

    # Extract painting titles
    title_element = soup.find('div', {'class': 'short-title'})
    if title_element:
        details['Title'] = title_element.get_text(strip=True)

    # Extract artist, artist dates, date made, inventory number and location
    for dt in soup.find_all('dt'):
        label = dt.get_text(strip=True)
        dd = dt.find_next_sibling('dd')

        if label == 'Artist' and dd:
            details['Artist'] = dd.get_text(strip=True)
        elif label == 'Artist dates' and dd:
            details['Artist dates'] = dd.get_text(strip=True)
        elif label == 'Date made' and dd:
            details['Date made'] = dd.get_text(strip=True)
        elif label == 'Inventory number' and dd:
            details['Inventory number'] = dd.get_text(strip=True)
        elif label == 'Location' and dd and dd.find('a'):
            details['Location'] = dd.find('a').get_text(strip=True)
    
    # Extract thumbnail url
    image_divs = soup.find_all('div', class_='image')
    for div in image_divs:
        style = div.get('style')
        if style and 'background-image' in style:
            details['Thumbnail URL'] = get_thumbnail_url(style)

    return details