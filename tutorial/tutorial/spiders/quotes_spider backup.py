import scrapy
from ..items import TutorialItem
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser


class QuotesSpider(scrapy.Spider):
    name = "login"
    page_number = 1
    
    start_urls = [
        "http://quotes.toscrape.com/login"
    ]

    def parse(self, response):
        token = response.css('form input::attr(value)').get()
        return FormRequest.from_response(response=response,formdata={
            'csrf_token' : token,
            'username':'vineedbiju@gmail.com',
            'password':"RandomPassword"
        }, callback = self.start_scraping)
        
    def start_scraping(self,response):
        open_in_browser(response)
        Items = TutorialItem()
        for quote in response.css("div.quote"):
            Items['Text'] = quote.css("span.text::text").get()
            Items['Author'] = quote.css("small.author::text").get()
            Items['Tags'] = quote.css("div.tags a.tag::text").getall()
            yield Items
        
        next_page = f"https://quotes.toscrape.com/page/{QuotesSpider.page_number}/"
        if QuotesSpider.page_number<11:
            QuotesSpider.page_number+=1
            yield response.follow(next_page,callback= self.start_scraping)