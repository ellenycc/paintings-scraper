from ngscraper.sitemap import get_paintings_urls
from ngscraper.scraper import extract_painting_details
import pandas as pd
import time

def main():
  painting_urls = get_paintings_urls()
  painting_urls = painting_urls[:10]

  all_data = []
  for i, url in enumerate(painting_urls):
      print(f'[{i+1}/{len(painting_urls)}] Scraping: {url}')
      data = extract_painting_details(url)
      all_data.append(data)
      time.sleep(1)

  df = pd.DataFrame(all_data)
  df.to_excel('output/paintings_data.xlsx', index=False)
  print('Data saved to outpput/paintings_data.xlsx')

if __name__ == "__main__":
    main()