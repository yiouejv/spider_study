# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'  # 爬虫名，运行爬虫时的名字
    allowed_domains = ['www.baidu.com']  # 允许爬取的域名
    start_urls = ['http://www.baidu.com/']  # 开始要爬取的url

    # parse 函数名不能改
    def parse(self, response):
        with open('baidu.html', 'w', encoding='utf-8') as wf:
            wf.write(response.text)
