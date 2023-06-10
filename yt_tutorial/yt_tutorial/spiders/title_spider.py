import scrapy

class QuoteSpider(scrapy.Spider):
    name = 'title_spider'
    start_urls = [
        'http://books.toscrape.com/'
    ]
    
    def parse(self, response):
        title = response.css('title::text').extract()
        yield {
            'title_text': title
        }
        return super().parse(response)
