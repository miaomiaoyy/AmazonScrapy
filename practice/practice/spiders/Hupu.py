# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from practice.items import HupuItem

class HupuSpider(scrapy.Spider):
    name = 'Hupu'
    # allowed_domains = ['bbs.hupu.com']
    # start_urls = ['http://bbs.hupu.com/']

    def start_requests(self):
        url = "https://bbs.hupu.com/bxj"
        url2 = "https://leetcode.com/api/problems/all/"
        yield Request(url=url)

    def parse(self, response):
        body = response.body

        # titles = response.xpath("//ul[@class='for-list']/li/div[1]/a/text()") html use Xpath to parse
        #use json parse

        for title in titles:
            hupuItem = HupuItem()
            hupuItem["title"] = title.extract()
            #print (title.extract())
            yield hupuItem



