from ngscraper.sitemap import get_paintings_urls
import pytest

MOCK_SITEMAP_XML = """
<urlset>
  <url><loc>https://www.nationalgallery.org.uk/paintings/test-painting-1</loc></url>
  <url><loc>https://www.nationalgallery.org.uk/paintings/test-painting-2</loc></url>
  <url><loc>https://www.nationalgallery.org.uk/paintings/glossary/some-glossary-page</loc></url>
  <url><loc>https://www.nationalgallery.org.uk/paintings/picture-of-the-month/some-picture-of-the-month-page</loc></url>
  <url><loc>https://www.nationalgallery.org.uk/paintings/catalogues/some-catalogues-page</loc></url>
  <url><loc>https://www.nationalgallery.org.uk/paintings/learn-about-art/some-learn-about-art-page</loc></url>
</urlset>
"""

EXCLUDE_KEYWORDS = ['/glossary/', '/picture-of-the-month/', '/catalogues/', '/learn-about-art/']

def test_get_paintings_urls(requests_mock):
  requests_mock.get(
    "https://www.nationalgallery.org.uk/xml-sitemap",
    text=MOCK_SITEMAP_XML
  )

  urls = get_paintings_urls()

  assert isinstance(urls, list)
  assert len(urls) == 2
  assert urls[0] == "https://www.nationalgallery.org.uk/paintings/test-painting-1"
  assert all(
    not any(keyword in url for keyword in EXCLUDE_KEYWORDS)
    for url in urls
  )
