# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookscraperItem(scrapy.Item):
    # Book content
    title = scrapy.Field()
    price = scrapy.Field()
    availability = scrapy.Field()



class QuoteItem(scrapy.Item):
    # Quote content
    text = scrapy.Field()
    author = scrapy.Field()
    author_about = scrapy.Field()
    author_born_date = scrapy.Field()
    author_born_location = scrapy.Field()
    author_description = scrapy.Field()
    tags = scrapy.Field()