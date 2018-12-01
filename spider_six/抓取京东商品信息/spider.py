#encoding: utf-8
import time

from selenium import webdriver
import csv
from lxml import etree

options = webdriver.ChromeOptions()
options.set_headless()

broswer = webdriver.Chrome(options=options)
broswer.get('http://www.jd.com/')


'''
    把下拉菜单拉到最底部
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
'''


def search():
    print('正在打开京东首页')
    # kw = input('请输入要搜索的商品：')
    broswer.find_element_by_id('key').send_keys('爬虫')
    # 点击搜索
    broswer.find_element_by_class_name('button').click()


def parse_one_page():
    try:
        print('正在打开页面...')
        time.sleep(1)
        items = broswer.find_elements_by_xpath('//ul[@class="gl-warp clearfix"]//li')
        for item in items:
            item = item.text.split()
            book = {
                'price': item[0],
                'name': item[1],
                'comment': item[2],
                'publisher': item[3],
            }
            print(book)
    except Exception as err:
        parse_one_page()


def main():
    search()
    parse_one_page()


if __name__ == '__main__':
    main()


