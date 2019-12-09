# _*_ coding=UTF-8 _*_
# 作者：Ariel
# 创建时间：2019-12-04 9:40 

from scrapy import Selector

content = open('all.html', 'r', encoding="utf-8")

selecter = Selector(text=content.read())
lis = selecter.xpath('//li[@class="clearfix car_list_less ac_item"]')
print(len(lis))