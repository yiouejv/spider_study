#encoding: utf-8

from selenium import webdriver
from lxml import etree
import csv

options = webdriver.ChromeOptions()
options.set_headless()
driver = webdriver.Chrome(options=options)


def get_one_page(page):
    if page == 1:
        driver.get('http://www.douyu.com/')
        # 点击"直播"菜单
        driver.find_element_by_link_text('直播').click()
        html = driver.page_source
    else:
        html = get_next_page()
    print('获取第%s页成功' % page)
    return html


def to_csv(row):
    with open('douyu.csv', 'a', encoding='gbk', newline='') as wf:
        writer = csv.writer(wf)
        writer.writerow(row)


def parse_one_page(html):
    parse_html = etree.HTML(html)
    # 拿到xpath匹配到的对象
    names = parse_html.xpath('//ul[@id="live-list-contentbox"]//span[@class="dy-name ellipsis fl"]')
    # 获取主播名称
    names = [name.text for name in names]
    focus = parse_html.xpath('//ul[@id="live-list-contentbox"]//span[@class="dy-num fr"]')
    focus = [focu.text for focu in focus]
    items = dict(zip(names, focus))
    for name, focu in items.items():
        to_csv([name, focu])


def get_next_page():
    driver.find_element_by_link_text('下一页').click()
    html = driver.page_source
    return html


def main():
    for page in range(1, 10):
        html = get_one_page(page)
        parse_one_page(html)
        print('成功解析%s页' % page)


if __name__ == '__main__':
    main()