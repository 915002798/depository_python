# _*_ coding=UTF-8 _*_
# 作者：Ariel
# 创建时间：2019-12-04 10:09
import re

from scrapy import Selector

file = open('li.html', 'r', encoding='utf-8')

li = Selector(text=file.read())
brand = li.css('.info_tit').xpath('.//font/text()').get()  # 品牌
title = re.compile('</font>(.*?)\n').findall(li.get())[0]  # 标题
info = li.css('.info_param').xpath('.//span/text()').getall()
start_time = info[0]  # 首次上牌时间
distance = info[1]  # 里程
volunme = info[2]  # 油耗
gear = info[3]  # 变速器
tag = '_'.join(li.css('.tags_left').xpath('.//em[@class="emShow"]/text()').getall())    # 标签
price = li.xpath('.//div[@class="col col3"]/h3/text()').get()    # 价格（单位：万）
print(price)
