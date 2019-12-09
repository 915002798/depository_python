# -*- coding: utf-8 -*-
import re

import scrapy

from ershouche.items import ErshoucheItem


class CarSpider(scrapy.Spider):
    name = 'car'
    allowed_domains = ['bj.58.com']
    url_template = 'http://bj.58.com/ershouche/pn{page}/'
    # start_urls = ['http://bj.58.com/ershouche/']

    def start_requests(self):
        for page in range(1, 71):
            url = self.url_template.format(page=page)
            print(url)
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        lis = response.xpath('//li[@class="clearfix car_list_less ac_item"]')

        for li in lis:
            item = ErshoucheItem()
            item['brand'] = li.css('.info_tit').xpath('.//font/text()').get()  # 品牌
            item['title'] = re.compile('</font>(.*?)\n').findall(li.get())[0]  # 标题
            info = li.css('.info_param').xpath('.//span/text()').getall()
            item['start_time'] = info[0]  # 首次上牌时间
            item['distance'] = info[1]  # 里程
            item['volume'] = info[2]  # 油耗
            item['gear'] = info[3]  # 变速器
            item['tag'] = '_'.join(li.css('.tags_left').xpath('.//em[@class="emShow"]/text()').getall())  # 标签
            item['price'] = li.xpath('.//div[@class="col col3"]/h3/text()').get()  # 价格（单位：万）
            yield item
