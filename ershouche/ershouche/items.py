# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ErshoucheItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    brand = scrapy.Field()
    title = scrapy.Field()
    start_time = scrapy.Field()
    distance = scrapy.Field()
    volume = scrapy.Field()
    gear = scrapy.Field()
    tag = scrapy.Field()
    price = scrapy.Field()
