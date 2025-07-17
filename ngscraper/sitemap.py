import requests
from bs4 import BeautifulSoup
from typing import List, Optional

HEADERS = {'User-Agent': 'Mozilla/5.0'}
SITEMAP_URL = 'https://www.nationalgallery.org.uk/xml-sitemap'
EXCLUDE_KEYWORDS = ['/glossary/', '/picture-of-the-month/', '/catalogues/', '/learn-about-art/']

def get_paintings_urls(
    sitemap_url: str = SITEMAP_URL,
    headers: Optional[dict] = None,
    exclude_keywords: Optional[list] = None
) -> List[str]:
    """
    Fetches painting URLs from the National Gallery sitemap.

    Args:
        sitemap_url (str): URL of the sitemap to parse.
        headers (dict, optional): HTTP headers for the request.
        exclude_keywords (list, optional): List of substrings; URLs containing any are excluded.

    Returns:
        List[str]: List of painting URLs

    """

    headers = headers or HEADERS
    exclude_keywords = exclude_keywords or EXCLUDE_KEYWORDS

    response = requests.get(sitemap_url, headers=headers)
    soup = BeautifulSoup(response.content, 'xml')

    urls = []
    all_urls = soup.find_all('loc')
    for loc in all_urls:
        url = loc.get_text()
        if '/paintings/' in url and not any(keyword in url for keyword in exclude_keywords):
            urls.append(url)

    return urls