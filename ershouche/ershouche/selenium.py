# _*_ coding=UTF-8 _*_
# 作者：Ariel
# 创建时间：2019-12-04 15:17
from time import sleep

from scrapy.http import HtmlResponse
from selenium import webdriver


class Selenium(object):

    @classmethod
    def process_request(cls, request, spider):
        option_chrome = webdriver.ChromeOptions()
        option_chrome.binary_location = r"D:\girl\software\Google\Chrome\Application\chrome.exe"
        option_chrome.add_argument('--headless')
        option_chrome.add_argument('--no-startup-window')
        option_chrome.add_argument('--no-sandbox')
        driver = webdriver.Chrome(chrome_options=option_chrome)
        sleep(3)
        driver.get(request.url)
        content = driver.page_source.encode('utf-8')
        driver.quit()
        return HtmlResponse(request.url, encoding='utf-8', body=content, request=request)
