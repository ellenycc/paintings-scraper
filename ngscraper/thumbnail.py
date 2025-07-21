import re

base_url = "https://www.nationalgallery.org.uk"

def get_thumbnail_url(css_style: str) -> str:
    """
    Extract the thumbnail image URL from a painting page.
    """
    match = re.search(r"url\(['\"]?(.*?)['\"]?\)", css_style)
    if match:
        url = match.group(1)
        if url.startswith('/'):
            url = base_url + url
        return url
    return None