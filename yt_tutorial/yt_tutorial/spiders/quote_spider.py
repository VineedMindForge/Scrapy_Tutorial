import scrapy
from ..items import YtTutorialItem

class book_spider(scrapy.Spider):
    name = 'book_spider'
    start_urls = [
        'http://books.toscrape.com/'
    ]
    
    def parse(self, response):
        Items = YtTutorialItem()
        all_class_elements = response.css('.col-lg-3')
        for book in all_class_elements:
            book_name = book.css('img.thumbnail').xpath('@alt').extract()
            star_rating = book.css('.star-rating').xpath('@class').extract()
            price = book.css('.price_color::text').extract()
            
            Items['book_name'] = book_name 
            Items['star_rating'] = star_rating 
            Items['price'] = price 

            yield Items
