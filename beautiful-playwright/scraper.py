from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

def get_html_with_playwright(url):
    print(f"getting html from with playwright {url}")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url, wait_until='domcontentloaded')
        html_content = page.content()
        with open("index.html", "w") as file:
            file.write(html_content)
        print(html_content)
        browser.close()
        # Create and return the BeautifulSoup object
        soup = BeautifulSoup(html_content, 'lxml')
        if not soup:
            print("Warning: BeautifulSoup returned None")
        return soup