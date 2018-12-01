# -*- coding: utf-8 -*-
import scrapy
from ..items import CsdnItem

class CsdnSpider(scrapy.Spider):
    name = 'csdn_'
    allowed_domains = ['blog.csdn.net']
    start_urls = ['https://blog.csdn.net/csdnnews/article/details/84531513']

    def parse(self, response):
        item = CsdnItem()
        item.name = response.xpath('//h1[@class="title-article"]/text()').extract()[0]  # 标题
        item.time = response.xpath('//div[@class="article-bar-top"]//span[@class="time"]/text()').extract()[0]  # 发表时间
        item.read = response.xpath('//div[@class="article-bar-top"]//span[@class="read-count"]/text()').extract()[0]  # 阅读数
        yield item
