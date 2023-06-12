import scrapy
from ..items import AmazonScrapeItem


class ScrapeAmazonSpider(scrapy.Spider):
    name = "scrape_amazon"
    allowed_domains = ["amazon.com"]
    start_urls = [
        "https://www.amazon.in/s?rh=n%3A4771382031&fs=true&ref=lp_4771382031_sar"
        ]

    def parse(self, response):
        items = AmazonScrapeItem()
        for item in response.css('.s-card-border'):
            items['title'] = item.css('.a-color-base.a-text-normal::text').get()
            items['price'] = item.css('span.a-price-whole::text').get()
            items['price_per_item'] = item.css('.a-price+ .a-color-secondary::attr(html)').get()
            items['image'] = item.css('.s-image::attr(src)').get()
            items['rating'] = item.css('div.a-row a-size-small span::attr(aria-label)').get()
            items['review'] = item.css('aria-label::attr(html)').get()
            
            yield items

    
