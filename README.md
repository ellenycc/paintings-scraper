# National Gallery Painting Scraper

**Automated data extraction tool built to streamline art collection documentation at The National Gallery (London)**

---

## 👩‍💻 About the Project

As a Digital Administrator at The National Gallery, I developed this web scraping script to address a real-world need: consolidating metadata for over 2,500 paintings into a centralised, searchable database. This project demonstrates my ability to:

- Automate repetitive manual tasks with Python
- Work with structured and unstructured web data
- Apply technical solutions to improve team workflows
- Build tools that scale across departments

---

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

---

## Tech Stack

| Tool/Library   | Purpose                           |
|----------------|------------------------------------|
| Python 3       | Core language                     |
| `requests`     | Making HTTP requests              |
| `BeautifulSoup`| HTML/XML parsing                  |
| `pandas`       | Data formatting & Excel export    |
| `pytest`       | Automated testing                 |
| `requests-mock`| Mocking web requests in tests     |

---

## Project Structure

```
ng-scraper/
├── main.py                # Entry point for the scraper
├── ngscraper/
│   ├── __init__.py
│   ├── scraper.py         # Core scraping logic
│   └── sitemap.py         # Sitemap parsing utilities
├── output/                # Output Excel files
├── tests/                 # Test suite
├── Pipfile                # Dependency management
├── setup.py               # Package configuration
└── README.md
```

---

## Impact

✅ Reduced hours of manual data entry  
✅ Created a scalable solution that can be extended to include image data and AI features
✅ Demonstrated practical application of software development in a museum environment

---

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


## Testing

To run the test suite (requires `pytest` and `requests-mock`):

```bash
pipenv install --dev pytest requests-mock
pytest
```

## Troubleshooting

- **ModuleNotFoundError:** Make sure you have installed the package in editable mode:
  ```bash
  pip install -e .
  ```
- **Missing dependencies:** Ensure you have run `pipenv install`.
- **Output directory error:** If you get an error about the `output/` directory, create it manually or ensure the script creates it.


## Future Additions
- Image metadata extractor (TIFF, PSB pixel dimensions)
- AI-powered image tagging (e.g. subjects, styles, artists)
- Web UI to browse and search the collection

## About Me
This project is part of my journey transitioning into software engineering.
If you're interested in collaborating or want to chat about automation, cultural tech, or applying Python in the arts, feel free to reach out on GitHub[https://github.com/ellenycc] or connect on LinkedIn[https://www.linkedin.com/in/ellen-chan-01656731/]!