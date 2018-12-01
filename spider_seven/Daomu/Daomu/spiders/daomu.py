# -*- coding: utf-8 -*-
import scrapy
from ..items import DaomuItem
from lxml import etree


class DaomuSpider(scrapy.Spider):
    name = 'daomu'
    allowed_domains = ['daomubiji.com']
    start_urls = ['http://www.daomubiji.com/dao-mu-bi-ji-1']

    def parse(self, response):
        item = DaomuItem()
        parse_html = etree.HTML(response.text)
        item.title = parse_html.xpath('//h1[@class="focusbox-title"]/text()')
        item.zhangjie = parse_html.xpath('//article[@class="excerpt excerpt-c3"]//a/text()')
        item.href = parse_html.xpath('//article[@class="excerpt excerpt-c3"]//a/@href')
        with open('xx.csv', 'w') as wf:
            wf.write(item.title+item.zhangjie+item.href)
            wf.write('xx')
        yield item
