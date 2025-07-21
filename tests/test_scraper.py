import pytest
from ngscraper.scraper import extract_painting_details

MOCK_HTML = """
<html>
  <body>
    <div class="short-title">The Mocked Title</div>
    <dl>
      <div class="list-row">
        <dt>Artist</dt>
        <dd><a href="#">Mocked Artist</a></dd>
      </div>
      <div class="list-row">
        <dt>Artist dates</dt>
        <dd>1900 - 1950</dd>
      </div>
      <div class="list-row">
        <dt>Date made</dt>
        <dd>1923</dd>
      </div>
      <div class="list-row">
        <dt>Inventory number</dt>
        <dd>NG123</dd>
      </div>
      <div class="list-row">
        <dt>Location</dt>
        <dd><a href="#">Room 1</a></dd>
      </div>
    </dl>
    <div class="image-container">
    <div class="image"
      style="background-image: url('/default.jpg');">
    </div>
    </div>
  </body>
</html>
"""

def test_extract_painting_details(requests_mock):
    url = "https://www.nationalgallery.org.uk/paintings/mock-painting"
    requests_mock.get(url, text=MOCK_HTML)
    result = extract_painting_details(url)
    assert result['Title'] == 'The Mocked Title'
    assert result['Artist'] == 'Mocked Artist'
    assert result['Artist dates'] == '1900 - 1950'
    assert result['Date made'] == '1923'
    assert result['Inventory number'] == 'NG123'
    assert result['Location'] == 'Room 1'
    assert result['Painting URL'] == url
    assert result['Thumbnail URL'] == 'https://www.nationalgallery.org.uk/default.jpg'