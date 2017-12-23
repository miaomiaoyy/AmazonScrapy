import scrapy
from scrapy import Request
from bs4 import BeautifulSoup
from practice.items import AppleItem


class AppleCrawler(scrapy.Spider):
    name = 'apple'

    def start_requests(self):
        start_url = "https://hk.appledaily.com/realtime/realtimelist/us?page=us"
        yield Request(url=start_url)

    def parse(self, response):
        # res = BeautifulSoup(response.body, "lxml")
        # for news in res:
        #     print(news.extract())

        data = response.xpath("//div[@class=\'RTitemRHS\']/div[5]/a/text()")

        for each in data:
            print (each.extract())

        url = "aaa"
        yield Request(url=url, callback=self.parse_second_level)


    def parse_second_level(self, response):
        pass