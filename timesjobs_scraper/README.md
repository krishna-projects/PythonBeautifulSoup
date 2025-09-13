# TimesJobs Scraper

A Python-based web scraper for extracting job listings from TimesJobs.com.

## Project Structure

```
timesjobs_scraper/
├── config/           # Configuration files
├── data/             # Raw and processed data
│   ├── raw/         # Raw HTML responses
│   └── processed/   # Processed data (CSV, JSON)
├── logs/            # Log files
└── src/             # Source code
    ├── parser.py    # HTML parsing logic
    ├── scraper.py   # Web scraping logic
    └── storage.py   # Data storage functions
```

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure the following directories exist:
   - `data/raw/`
   - `data/processed/`
   - `logs/`

## Usage

Run the main script:
```bash
python main.py
```

## Configuration

Edit `config/settings.py` to modify:
- Base URL
- Search parameters
- Request headers
- CSS selectors

## Output

Job listings are saved in the `data/processed/` directory as CSV files with timestamps.

## Logging

Logs are stored in the `logs/` directory with daily rotation.
