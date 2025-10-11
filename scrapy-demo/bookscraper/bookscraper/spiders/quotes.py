import scrapy
from bookscraper.items import QuoteItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        for quote in response.css('div.quote'):
            author_about_url = response.urljoin(quote.css('small.author + a::attr(href)').get())
            request = scrapy.Request(author_about_url, callback=self.parse_author)
            request.meta['quote'] = {  # Pass the quote data to the callback
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('a.tag::text').getall(),
            }
            yield request
        
        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)


    def parse_author(self, response):
        quote = response.meta['quote']
        item = QuoteItem()

        item['text'] = quote['text']
        item['author'] = quote['author']
        item['tags'] = quote['tags']
        item['author_about'] = response.css('span.author-born-date::text').get()
        item['author_born_date'] = response.css('span.author-born-date::text').get()
        item['author_born_location'] = response.css('span.author-born-location::text').get()
        item['author_description'] = response.css('div.author-description::text').get().strip()
        
        yield item