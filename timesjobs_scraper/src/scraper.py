import requests
from typing import Optional
from bs4 import BeautifulSoup
from config.settings import BASE_URL, DEFAULT_PARAMS, HEADERS

class JobScraper:
    def __init__(self, base_url: str = None):
        self.base_url = base_url or BASE_URL
        self.session = requests.Session()
        self.session.headers.update(HEADERS)

    def fetch_jobs(self, params: Optional[dict] = None) -> str:
        """Fetch job listings from the website."""
        try:
            response = self.session.get(
                self.base_url,
                params=params or DEFAULT_PARAMS,
                timeout=10
            )
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching jobs: {e}")
            return ""

    def save_raw_html(self, content: str, filename: str) -> None:
        """Save raw HTML content to a file."""
        try:
            with open(f"data/raw/{filename}", 'w', encoding='utf-8') as f:
                f.write(content)
        except IOError as e:
            print(f"Error saving HTML: {e}")

    def close(self):
        """Close the session when done."""
        self.session.close()
