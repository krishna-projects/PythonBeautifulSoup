# BookScraper - A Scrapy Project for books.toscrape.com

This project demonstrates web scraping using Scrapy, focusing on extracting book information from books.toscrape.com. It serves as both a learning resource and a template for building production-ready scrapers.

## 🚀 Project Structure

```
bookscraper/
├── bookscraper/               
│   ├── __init__.py
│   ├── items.py              # Define item structures
│   ├── middlewares.py        # Custom middlewares
│   ├── pipelines.py          # Item pipelines for data processing
│   ├── settings.py           # Project settings
│   └── spiders/              # Directory for spiders
│       ├── __init__.py
│       └── books_spider.py   # Our main spider
└── scrapy.cfg                # Deploy configuration
```

## 🛠️ Prerequisites

- Python 3.7+
- Scrapy 2.13.3 (or later)
- (Optional) Jupyter Notebook for data analysis

## 🏁 Getting Started

1. **Install Scrapy** (if not already installed):
   ```bash
   pip install scrapy
   ```

2. **Create a new Scrapy project**:
   ```bash
   scrapy startproject bookscraper
   cd bookscraper
   ```

3. **Create a spider**:
   ```bash
   scrapy genspider books books.toscrape.com
   ```

## 🕷️ Running Spiders

### Basic Spider Execution
```bash
# Run the spider and save output to JSON
scrapy crawl books -o books.json

# Run the spider and save output to CSV
scrapy crawl books -o books.csv

# Run spider with debug logging
scrapy crawl books -s LOG_LEVEL=DEBUG
```

### Advanced Usage
```bash
# Limit the number of pages to scrape
scrapy crawl books -s CLOSESPIDER_PAGECOUNT=5

# Follow specific settings
scrapy crawl books -s DOWNLOAD_DELAY=2 -s CONCURRENT_REQUESTS=4

# Run with specific output format
scrapy crawl books -o books.jl  # JSON Lines format
```

## 🔍 Spider Development

### Creating a New Spider
```python
import scrapy

class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        for book in response.css('article.product_pod'):
            yield {
                'title': book.css('h3 a::attr(title)').get(),
                'price': book.css('p.price_color::text').get(),
                'availability': book.css('p.availability::text')[1].get().strip(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
```

## ⚙️ Project Configuration (`settings.py`)

Key settings to customize:

```python
# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure item pipelines
ITEM_PIPELINES = {
    'bookscraper.pipelines.BookscraperPipeline': 300,
}

# Set download delay to respect the website
DOWNLOAD_DELAY = 1.5

# Configure maximum concurrent requests
CONCURRENT_REQUESTS = 4

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# User agent
USER_AGENT = 'bookscraper (+http://www.yourdomain.com)'
```

## 🔄 Item Pipeline

Example pipeline for data processing:

```python
class BookscraperPipeline:
    def process_item(self, item, spider):
        # Clean price data
        if 'price' in item:
            item['price'] = float(item['price'].replace('£', ''))
        return item
```

## 🧪 Testing Spiders

### Using Scrapy Shell
```bash
scrapy shell 
fetch('https://books.toscrape.com/')

# Example commands in shell:
# response.css('h1::text').get()
# response.xpath('//title/text()').get()
```

## 📦 Deploying to ScrapingHub (Optional)

1. Install shub:
   ```bash
   pip install shub
   ```

2. Login:
   ```bash
   shub login
   ```

3. Deploy:
   ```bash
   shub deploy
   ```

## 🛠️ Scrapy Methods Reference

### Basic Methods
- `scrapy.Spider`: Base class for all spiders
- `scrapy.Request`: For making HTTP requests
- `response.css()`: Select elements using CSS selectors
- `response.xpath()`: Select elements using XPath
- `response.get()`: Get first matching element (or default)
- `response.getall()`: Get all matching elements as a list
- `response.follow()`: Follow a link to a new page
- `response.urljoin()`: Convert relative URLs to absolute

### Spider Class Methods
- `start_requests()`: Generates initial requests
- `parse()`: Default callback for parsing responses
- `closed()`: Called when spider closes
- `log()`: Log a message
- `from_crawler()`: Class method to get crawler object

### Response Methods
- `response.url`: URL of the response
- `response.status`: HTTP status code
- `response.headers`: Response headers
- `response.text`: Response body as string
- `response.body`: Raw response bytes
- `response.css()`: Select elements with CSS
- `response.xpath()`: Select elements with XPath
- `response.json()`: Parse response as JSON

### Selector Methods
- `.get()`: Get first matching element
- `.getall()`: Get all matching elements
- `.re()`: Extract data using regex
- `.re_first()`: First regex match
- `.attrib`: Get element attributes
- `.extract()`: Alias for getall() (older versions)

### Item Pipeline Methods
- `process_item()`: Process each item
- `open_spider()`: Called when spider is opened
- `close_spider()`: Called when spider is closed
- `from_crawler()`: Get crawler object

### Middleware Methods
- `process_request()`: Process each request
- `process_response()`: Process each response
- `process_exception()`: Handle exceptions
- `from_crawler()`: Get crawler object

### Running Spiders
```bash
# Basic run
scrapy crawl spider_name

# Save output to file
scrapy crawl spider_name -o output.json

# Follow specific settings
scrapy crawl spider_name -s LOG_LEVEL=INFO

# Run with custom settings module
scrapy crawl spider_name -s SETTINGS_MODULE=myproject.settings
```

### Scrapy Shell
```bash
# Start shell with URL
scrapy shell 'http://example.com'

# In shell:
# response.css() - CSS selection
# response.xpath() - XPath selection
# view(response) - View in browser
# fetch(url) - Fetch new URL
# shelp() - Show help
```

### Common Selector Examples
```python
# Get text
response.css('h1::text').get()

# Get attribute
response.css('a::attr(href)').get()

# Get all matching elements
response.css('.product').getall()

# XPath examples
response.xpath('//h1/text()').get()
response.xpath('//a/@href').get()
```

### Item Exporters
- `JsonItemExporter`: Export to JSON
- `JsonLinesItemExporter`: Export to JSON Lines
- `CsvItemExporter`: Export to CSV
- `XmlItemExporter`: Export to XML

### Built-in Services
- `scrapy.Spider`: Base spider
- `scrapy.crawler.Crawler`: Main crawler
- `scrapy.settings`: Project settings
- `scrapy.item`: Item and Field classes
- `scrapy.selector`: Selector classes
- `scrapy.linkextractors`: Link extraction
- `scrapy.signalmanager`: Signal handling
```

## 📚 Learning Resources

- [Scrapy Documentation](https://docs.scrapy.org/)
- [Scrapy Tutorial](https://docs.scrapy.org/en/latest/intro/tutorial.html)
- [CSS Selectors Reference](https://www.w3schools.com/cssref/css_selectors.asp)
- [XPath Cheatsheet](https://devhints.io/xpath)

## 🤝 Contributing

Feel free to submit issues and enhancement requests.

## 📄 License

This project is licensed under the MIT License.
