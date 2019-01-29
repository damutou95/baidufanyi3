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
        with open('/home/xiyujing/baidufanyi2/歌词.txt', 'r') as f:
            lines = f.readlines()
        for line in lines:
            kw = parse.quote(line.strip())
            print(kw)
            print('$$$$$$$$$$$$')
            url = self.start_urls[0] + kw
            print(url)
            yield SplashRequest(url=url, callback=self.parse, headers=self.headers, args={'wait': 5})

    def parse(self, response):
        print(response.text)
        item = BaidufanyiItem()
        item['origin'] = response.xpath('//p[@class="ordinary-output source-output"]/text()').extract_first()
        item['translation'] = response.xpath('string(//p[@class="ordinary-output target-output clearfix"])').extract_first()
        return item
