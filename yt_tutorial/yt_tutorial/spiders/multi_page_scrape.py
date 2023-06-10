import scrapy
from ..items import YtTutorialItem

class MultipageScrape(scrapy.Spider):
    name = 'multi_page_spider'
    page_number = 2
    start_urls = [
        'https://books.toscrape.com/catalogue/page-1.html'
    ]
    
    def parse(self, response,):
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
        next_page = f'https://books.toscrape.com/catalogue/page-{MultipageScrape.page_number}.html'
        
        if MultipageScrape.page_number<=10:
            MultipageScrape.page_number+=1
            yield response.follow(next_page,callback=self.parse)