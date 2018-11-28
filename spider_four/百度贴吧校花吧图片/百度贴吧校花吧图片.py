#encoding: utf-8
from random import choice

from lxml import etree
import requests
from user_agent import agents_list_pc


class XHSpider():
    Base_url = 'http://tieba.baidu.com/f?pn'
    def __init__(self, page_start=1, page_stop=2, proxies=None):
        self.page_start = page_start
        self.page_stop = page_stop
        self.headers = {'User-Agent': "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
        self.proxies = proxies
        self.params = {
            'kw': '校花',
        }


    def get_page_html(self, page):
        '''获得当前页的html'''
        url = self.Base_url + str((page - 1) * 50)
        html = requests.get(url, params=self.params).text
        print('成功拿到%d页的html代码' % page)
        return html


    def get_html_urls(self, html):
        '''从当前页中获取所有的贴子url'''
        xpath = r"//div[@class='t_con cleafix']/div/div/div/a/@href"
        parse_html = etree.HTML(html)
        hrefs = parse_html.xpath(xpath)
        urls = ['http://tieba.baidu.com'+url for url in hrefs]
        print('当前页中有以下帖子：', urls[:-1])
        return urls[:-1]


    def get_img_urls(self, urls):
        '''从具体的页面中拿到图片地址'''
        imgurls = []  # 保存所有图片的url
        for url in urls:
            html = requests.get(url=url, headers=self.headers).text
            parse_html = etree.HTML(html)
            img_urls = parse_html.xpath(r'//img[@class="BDE_Image"]/@src')
            print(img_urls)
            imgurls.extend(img_urls)
        else:
            print('get_img_urls', '传入的urls为空')
        return imgurls


    def imguls_to_file(self, urls):
        for i, url in enumerate(urls, 1):
            content = requests.get(url, headers=self.headers).content
            filename = url[-12:]
            with open(filename, 'wb') as wf:
                wf.write(content)
            print(url, '下载成功')



    def worker(self):
        for page in range(self.page_start, self.page_stop):
            html = self.get_page_html(page)
            urls = self.get_html_urls(html)
            img_urls = self.get_img_urls(urls)
            self.imguls_to_file(img_urls)



if __name__ == '__main__':
    xh = XHSpider(1, 3)
    xh.worker()
