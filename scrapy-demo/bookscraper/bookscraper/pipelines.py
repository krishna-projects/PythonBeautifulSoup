# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BookscraperPipeline:
    def process_item(self, item, spider):
         # Get the request from the spider
        request = getattr(spider, 'request', None)
        
        if request:
            current_url = request.url
            parsed_url = urlparse(current_url)
            
            # Log the full URL and domain
            spider.logger.info(f"Processing URL: {current_url}")
            spider.logger.info(f"Domain: {parsed_url.netloc}")
            spider.logger.info(f"Path: {parsed_url.path}")
            
            
        return item
