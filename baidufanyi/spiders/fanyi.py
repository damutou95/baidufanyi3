# -*- coding: utf-8 -*-
import scrapy
from urllib import parse
from scrapy_splash import SplashRequest
from baidufanyi import settings
from baidufanyi.items import BaidufanyiItem


class FanyiSpider(scrapy.Spider):
    name = 'fanyi'
    start_urls = ['https://fanyi.baidu.com/?aldtype=16047#zh/en/']
    headers = settings.HEADERS

    def start_requests(self):
        with open('/home/xiyujing/文档/测试.txt', 'r') as f:
            lines = f.readlines()
        for line in lines:
            kw = parse.quote(line.strip())
            url = self.start_urls[0] + kw
            yield SplashRequest(url=url, callback=self.parse, headers=self.headers, args={'wait': 5})

    def parse(self, response):
        item = BaidufanyiItem()
        item['origin'] = response.xpath('//p[@class="ordinary-output source-output"]/text()').extract_first()
        item['translation'] = response.xpath('string(//p[@class="ordinary-output target-output clearfix"])').extract_first()
        return item
