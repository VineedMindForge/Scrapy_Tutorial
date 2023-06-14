import scrapy

class BookspiderSpider(scrapy.Spider):
    name = 'bookspider'
    start_urls = [
        'https://books.toscrape.com/'
    ]
    
    def parse(self, response):
        books = response.css('.col-lg-3')
        
        for book in books:
            
            book_link_element = book.css('h3 a::attr(href)').get()
            if 'catalogue/' in book_link_element:
                book_link = 'https://books.toscrape.com/' + book_link_element
            else:
                book_link = 'https://books.toscrape.com/catalogue/' + book_link_element
                
            yield response.follow(book_link,callback = self.parse_book_link)
            
        next_page_element = response.css('li.next a::attr(href)').get()
        
        if next_page_element is not None:
            if 'catalogue/' in next_page_element:
                next_page = 'https://books.toscrape.com/' + next_page_element
            else:
                next_page = 'https://books.toscrape.com/catalogue/' + next_page_element
            
            yield response.follow(next_page,callback = self.parse)
        
        
            
    def parse_book_link(self,response):
        yield {
            "book_title":response.css('div.col-sm-6:nth-child(2) > h1:nth-child(1)::text').extract(),
            "price":response.css('p.price_color::text').get(),
            # "stock_status": response.css('div.col-sm-6:nth-child(2)').get(),
            'category':response.css('.breadcrumb li~ li+ li a::text').get(),
            'star_rating':response.css('.star-rating').attrib['class']            
        }