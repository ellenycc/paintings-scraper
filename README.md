# National Gallery Painting Scraper

A Python script that automates the extraction of painting information from [The National Gallery, London](https://www.nationalgallery.org.uk), which contributed to a comprehensive database of the Gallery's collection.

## Why I Built This

Our team needed a centralised, easily accessible list of paintings to support internal planning and reference. I built this script to:

- Automate the collection of data from over **2,500 paintings**
- Compile key painting details into a **single Excel file**
- Improve the efficiency of manual lookup and documentation tasks

This project not only improved efficiency in our internal workflow but also gave me hands-on experience using Python to solve a real-world problem in a cultural and digital context.

The script significantly improved efficieny in our internal workflow,and enabled the team to establish a complete, accurate, and easily accessible database of the Gallery’s collection.

## What it does

- Visits each painting page found in the sitemap
- Extracts details including:
  - Painting title
  - Artist and artist dates
  - Date made
  - Inventory number
  - Display Location
  - URL to the painting pages
- Compiles all results into an Excel spreadsheet

## Built With

- Python 3
- `requests` for HTTP requests
- `BeautifulSoup` for HTML parsing
- `pandas` and `openpyxl` for Excel export

## How to Run

### 1. Clone the repo:

```bash
git clone https://github.com/ellenycc/paintings-scraper.git
cd paintings-scraper
```

### 2. Install dependencies

```bash
pipenv install
pipenv shell
```

### 3. Run the script

```bash
python main.py
```

Your output will be saved to:

```bash
output/paintings_data.xlsx
```
