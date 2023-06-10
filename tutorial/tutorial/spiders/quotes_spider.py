import scrapy
from ..items import TutorialItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    page_number = 2
    start_urls = [
        "https://quotes.toscrape.com/page/1/"
    ]

    def parse(self, response):
        Items = TutorialItem()
        for quote in response.css("div.quote"):
            Items['Text'] = quote.css("span.text::text").get()
            Items['Author'] = quote.css("small.author::text").get()
            Items['Tags'] = quote.css("div.tags a.tag::text").getall()
            yield Items
        
        next_page = f"https://quotes.toscrape.com/page/{QuotesSpider.page_number}/"
        if QuotesSpider.page_number<11:
            QuotesSpider.page_number+=1
            yield response.follow(next_page,callback= self.parse)