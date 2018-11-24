#encoding: utf-8

# 1. 找URL规则
# 2. 用正则匹配出题目和答案
# 3. 写代码
#   1. 发请求
#   2. 解析
#   3. 保存
from urllib.request import urlopen, Request
from user_agent import agents_list_pc
from random import choice
import re
import sys, os



def get_url(page):
    '''
        传入页码，返回具体的url
    :param page: 页码
    :return: url地址
    '''
    BASE_URL = 'https://www.neihan8.com/njjzw/index_%d.html'
    try:
        if int(page):
            page = int(page)
    except Exception as err:
        raise ValueError('参数page应该为一个可转换int的值')
    if page == 1:
        url = 'https://www.neihan8.com/njjzw/index.html'
    elif page > 1:
        url = BASE_URL % page
    else:
        raise ValueError('参数page的值应该为大于等于0的数')
    return url


def get_html(url):
    '''
        传入一个url地址获取url的html文本
    :param url: 目标地址
    :return: 目标的html文本
    '''
    request = Request(
        url=url,
        headers={
            'User-Agent': choice(agents_list_pc)
        }
    )
    try:
        response = urlopen(request)
        html = response.read().decode()
        return html
    except Exception as err:
        sys.exit(err)


def get_njjzw_dict(html):
    '''
        传入html文本，返回脑筋急转弯的字典
    :param html: html文本
    :return: 字典
    '''
    pattern = r'<div class="text-column-item box box-790">.*?<h3><a .*? title="(.*?)">.*?</a>.*?<div class="desc">(.*?)</div>'
    lst = re.findall(pattern, html, flags=re.S)
    items = {key.strip():value.strip() for key, value in lst}
    return items


def items_to_file(items):
    '''
        传入一个字典，把字典保存为文件
    :param items: 字典
    :return: None
    '''
    for key, value in items.items():
        with open('njjzw.csv', 'a', encoding='utf-8') as wf:
            wf.write(key+':'+value+',\n')


def main():
    for page in range(1, 200):
        url = get_url(page)
        print(url)
        html = get_html(url)
        items = get_njjzw_dict(html)
        items_to_file(items)
        print('第%s页成功' % page)


if __name__ == '__main__':
    main()