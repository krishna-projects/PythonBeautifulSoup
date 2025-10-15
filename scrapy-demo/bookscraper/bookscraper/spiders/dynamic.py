from scrapy import Request
from scrapy.spiders import Spider
from urllib.parse import urlparse
from bookscraper.items import ProductItem
from scrapy_playwright.page import PageMethod
from bs4 import BeautifulSoup

class DynamicSpider(Spider):
    name = "dynamic"
    
    # List of domains that require Playwright
    PLAYWRIGHT_DOMAINS = ['shop.lululemon.com']
    
    # Start with a list of URLs that might need different handlers
    start_urls = [
        'https://quotes.toscrape.com/',
    ]
    
    def start_requests(self):
        for url in self.start_urls:
            yield self.create_request(url, self.parse)
    
    def create_request(self, url, callback):
        """Create a request with appropriate settings based on domain"""
        domain = urlparse(url).netloc
        
        if domain in self.PLAYWRIGHT_DOMAINS:
            # Use Playwright for JavaScript-heavy sites
            return Request(
                url,
                callback=callback,
                meta={
                    "playwright": True,
                    "playwright_include_page": True,
                    "playwright_page_methods": [
                        PageMethod("wait_for_selector", "h1"),
                    ],
                    "playwright_context_kwargs": {
                        "ignore_https_errors": True,
                    },
                },
            )
        else:
            # Use standard Scrapy for simple sites
            return Request(url, callback=callback)
    
    def parse(self, response):
        self.logger.info(f"Request Headers from parse: {response.request.headers}")
        self.logger.info(f"Response type: {type(response.body)}")
        self.logger.info(f"Response preview: {response.body[:200]}")
            
        # Close Playwright page if it was used
        if "playwright_page" in response.meta:
            page = response.meta["playwright_page"]
            page.close()

        title = response.css("h1 a::text").get()
        self.logger.info(f"Title: {title}")
        
       