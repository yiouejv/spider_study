#encoding: utf-8
import time
from queue import Queue
from threading import Thread
from selenium import webdriver
import requests
from lxml import etree
from user_agent import agents_list_pc


class BuDeJieSpider():
    def __init__(self, page_start=1, page_stop=100):
        self.base_url = 'http://www.budejie.com/'
        self.headers = {
            'User-Agent': agents_list_pc[1],
        }
        self.page_start = page_start
        self.page_stop = page_stop
        self.url_queue = Queue()  # url 队列
        self.html_queue = Queue()  # 响应的html队列

    def get_url(self):
        '''获取url, 放入url队列'''
        for page in range(self.page_start, self.page_stop):
            url = self.base_url + str(page)
            self.url_queue.put(url)


    def get_html(self):
        '''获取请求得到的html源码, 存入解析队列'''
        while not self.url_queue.empty():
            html = requests.get(
                url=self.url_queue.get(),
                headers=self.headers
            ).text
            self.html_queue.put(html)
            # 清除此任务
            self.url_queue.task_done()


    def parse_html(self):
        '''解析一个页面的html'''
        while not self.html_queue.empty():
            html = self.html_queue.get()
            parse_html = etree.HTML(html)
            items = parse_html.xpath('//div[@class="j-r-list-c-desc"]//text()')
            for item in items:
                print(item.strip())
            # 清楚解析队列的任务
            self.html_queue.task_done()

    def worker(self):
        self.get_url()
        self.get_html()
        self.parse_html()

    def run(self):
        pass
        # 空列表存放线程列表
        th_lst = []
        # 生成url列表
        self.get_url()
        # 创建请求线程，放到列表中
        for _ in range(10):
            th = Thread(target=self.get_html())
            th_lst.append(th)
        # 创建解析线程，放到列表中
        for _ in range(10):
            th = Thread(target=self.parse_html())
            th_lst.append(th)
        # 所有线程开始工作
        for th in th_lst:
            th.setDaemon(True)
            th.start()

        # 如何队列为空，则执行其他程序
        self.url_queue.join()
        self.html_queue.join()


if __name__ == '__main__':
    begin = time.time()
    bdj = BuDeJieSpider(1, 100)
    bdj.run()
    stop = time.time()
    interval = stop - begin
    print(interval)
