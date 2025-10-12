import scrapy
from bookscraper.items import BookscraperItem

class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    # Custom settings for this spider
    # custom_settings = {
    #     'DEFAULT_REQUEST_HEADERS': {
    #         'Referer': 'https://www.google.com/',
    #     }
    # }


    def start_requests(self):
        headers = {
            'X-Custom-Header': 'custom-header-value',
            # Other headers you want to add/override
        }
        
        # Get default headers from settings
        default_headers = self.settings.getdict('DEFAULT_REQUEST_HEADERS', {})
        
        # Merge headers (custom headers take precedence)
        final_headers = {**default_headers, **headers}
        
        for url in self.start_urls:
            # Log request headers for debugging
            # or directly use extra headers
            self.logger.info(f"Request URL from start_requests: {url}")
            yield scrapy.Request(url,headers={'extra-header': 'test'},callback=self.parse)


    def parse(self, response):
         # Log request headers for debugging
        self.logger.info(f"Request Headers from parse: {response.request.headers}")
        self.logger.info(f"Response type: {type(response.body)}")
        self.logger.info(f"Response preview: {response.body[:200]}")
            
        for book in response.css('article.product_pod'):
            item = BookscraperItem()

            item['title'] = book.css('h3 a::attr(title)').get()
            item['price'] = book.css('p.price_color::text').get()
            item['availability'] = book.css('p.availability::text')[1].get().strip()

            yield item
            
        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
