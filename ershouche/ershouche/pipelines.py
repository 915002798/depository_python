# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv


class ErshouchePipeline(object):
    def __init__(self):
        self.file = open('data.csv', 'w', newline='', encoding='utf-8')
        self.writer = csv.writer(self.file)
        self.writer.writerow(['brand', 'title', 'start_time', 'distance', 'volume', 'gear', 'tag', 'price'])

    def process_item(self, item, spider):
        print("============================")
        print(item)
        print("====================================")
        self.writer.writerow([item['brand'], item['title'], item['start_time'], item['distance'], item['volume'],
                             item['gear'], item['tag'], item['price']])

    def close_spider(self):
        self.file.close()