# National Gallery Painting Scraper

**Automated data extraction tool built to streamline art collection documentation at The National Gallery**

## About the Project

As a Digital Administrator at The National Gallery, I built this automation script to consolidate the metadata for over 2,500 paintings into a centralised, searchable database. This project demonstrates my ability to:

- Automate repetitive manual tasks with Python
- Work with structured and unstructured web data
- Apply technical solutions to improve team workflows
- Build tools that scale across departments


## Features

- Automatically fetches individual painting page links via the National Gallery’s XML sitemap
- Extracts painting metadata, including:
  - Title
  - Artist
  - Artist Dates
  - Date Made
  - Inventory Number
  - Display Location
  - Page URL
- Saves structured data to Excel for team-wide access and archival
- Modular structure for easy extension (e.g. image resolution, AI tagging)


## Tech Stack

| Tool/Library   | Purpose                           |
|----------------|------------------------------------|
| Python 3       | Core language                     |
| `requests`     | Making HTTP requests              |
| `BeautifulSoup`| HTML/XML parsing                  |
| `pandas`       | Data formatting & Excel export    |
| `pytest`       | Automated testing                 |
| `requests-mock`| Mocking web requests in tests     |


## Project Structure

```
ng-scraper/
├── main.py                
├── ngscraper/
│   ├── __init__.py
│   ├── scraper.py        
│   └── sitemap.py         
├── output/                
├── tests/                 
├── Pipfile                
├── setup.py              
└── README.md
```


## Impact

✅ Reduced hours of manual data entry  
✅ Created a scalable solution that can be extended to include image data and AI features


## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/ellenycc/ng-scraper.git
cd ng-scraper
pipenv install
```

## Usage

Activate the virtual environment and run the scraper:

```bash
pipenv shell
python main.py
```

By default, the output Excel file will be saved in the `output/` directory as `paintings_data.xlsx`.

## Future Additions
- Image metadata extractor (TIFF, PSB pixel dimensions)
- AI-powered image tagging (e.g. subjects, styles, artists)
- Web UI to browse and search the collection