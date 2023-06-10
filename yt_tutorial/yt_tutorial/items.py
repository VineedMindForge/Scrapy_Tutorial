# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YtTutorialItem(scrapy.Item):
    # define the fields for your item here like:
    book_name = scrapy.Field()
    star_rating = scrapy.Field()
    price = scrapy.Field()
    
