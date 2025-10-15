from scrapy import Request
from scrapy.spiders import Spider
from urllib.parse import urlparse
from bookscraper.items import ProductItem
from scrapy_playwright.page import PageMethod

class DynamicSpider(Spider):
    name = "dynamic"
    
    # List of domains that require Playwright
    PLAYWRIGHT_DOMAINS = ['shop.lululemon.com']
    
    # Start with a list of URLs that might need different handlers
    start_urls = [
        'https://shop.lululemon.com/p/womens-outerwear/Womens-Big-Cozy-Ultra-Oversized-Full-Zip-Hood-Long/_/prod20004863?color=30210',
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
        domain = urlparse(response.url).netloc
        self.logger.info(f"Request Headers from parse: {response.request.headers}")
        self.logger.info(f"Response type: {type(response.body)}")
        self.logger.info(f"Response preview: {response.body[:200]}")
            
        # Close Playwright page if it was used
        if "playwright_page" in response.meta:
            page = response.meta["playwright_page"]
            page.close()
        
        # Route to appropriate parser based on domain
        if domain == "shop.lululemon.com":
            yield self.parse_lululemon(response)
        else:
            # For non-Playwright sites, we can use the sync parse_generic
            yield self.parse_generic(response)
    
    async def parse_lululemon(self, response):
        """Parse Lululemon product page with Playwright"""
        item = ProductItem()
        
        # Extract data using CSS selectors
        item['title'] = response.css('h1[data-testid="product-title"]::text').get()
        item['price'] = response.css('span[data-testid="product-price"]::text').get()
        item['color'] = response.css('span[data-testid="selected-style"]::text').get()
        item['description'] = ' '.join(response.css('div[data-testid="product-details"] *::text').getall())
        
        # Extract all available colors
        item['available_colors'] = response.css('button[data-testid^="swatch-"]::attr(aria-label)').getall()
        
        # Extract size chart if available
        size_chart = {}
        size_rows = response.css('table.size-chart tbody tr')
        for row in size_rows:
            cells = row.css('td::text').getall()
            if len(cells) >= 2:
                size_chart[cells[0].strip()] = cells[1].strip()
        item['size_chart'] = size_chart
        
        return item
    
    def parse_generic(self, response):
        """Default parser for non-Playwright sites"""
        # This is a simple example - customize as needed
        item = ProductItem()
        item['url'] = response.url
        item['title'] = response.css('title::text').get()
        item['content'] = ' '.join(response.css('body *::text').getall()[:500]) + '...'
        return item