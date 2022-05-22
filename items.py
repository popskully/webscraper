# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags

class ShopinjascrapeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_title = scrapy.Field()
    product_price = scrapy.Field()
    product_description = scrapy.Field()
    product_imagelink = scrapy.Field()
    view_count = scrapy.Field()
    ad_type = scrapy.Field()
    # product_imagelink2 = scrapy.Field()
    # product_imagelink3 = scrapy.Field()
    # product_imagelink4 = scrapy.Field()
    urls = scrapy.Field()
    product_author = scrapy.Field()
    # product_price = scrapy.Field()
    product_phone = scrapy.Field()
    product_location = scrapy.Field()
    product_active = scrapy.Field()

    # car features
    year = scrapy.Field()
    make = scrapy.Field()
    model = scrapy.Field()
    fuel = scrapy.Field()
    door = scrapy.Field()
    transm = scrapy.Field()
    body = scrapy.Field()
    driver_side = scrapy.Field()
    feature = scrapy.Field()

    # product_imagelink = scrapy.Field()
    # car_year = scrapy.Field()
    # car_make = scrapy.Field()
    # car_model = scrapy.Field()



# import scrapy
# from scrapy.loader.processors import MapCompose,TakeFirst
# from w3lib.html import remove_tags
#
# class ShopinjascrapeItem(scrapy.Item):
#     product_title = scrapy.Field(
#         input_processor= MapCompose(remove_tags),
#         output_processor= TakeFirst()
#     )