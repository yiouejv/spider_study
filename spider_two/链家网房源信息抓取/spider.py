#encoding: utf-8

#  抓取链家网二手房信息
# 地址：https://bj.lianjia.com/ershoufang/
# 保存到mongodb数据库
#     {
#   'iamge': 缩略图
#   'title': 二手房标题
#    name:  名称（如：月坛北街25号院）
#   'info': 房子的属性{
#           spec:  规格（如：二室一厅）
#           area:  面积（如：77.7平米）
#           orientation: 朝向（如: 南北）
#       }

#      floor: 楼层（如：顶层共xx楼/中层/底层）
#      time: 修建时间（如：2000年建板楼）
#      place: 地点（如: 月坛）
#    'focus': 关注量(如：445人关注)
#    'price': 单价(如：单价20000元/平米)
#    'total': 总价(如：690万元)
# }
import csv

import pymongo
import re
import sys
from random import choice
from user_agent import agents_list_pc
import requests

conn = pymongo.MongoClient('localhost', 27017)

def get_url(page):
    try:
        page=int(page)
    except Exception as err:
        sys.exit('page该为一个能被转换的数值')
    Base_url = 'https://bj.lianjia.com/ershoufang/'
    if page == 1:
        url = Base_url
    else:
        url = Base_url + ('pg%s/' % str(page))
    return url


def to_csv(item):
    with open('lianjia.csv', 'a', newline='') as wf:
        writer = csv.writer(wf)
        writer.writerow(list(item.values()))
    print('写入文件成功')


def get_index_page(url):
    '''传入一个url，返回一个该url的html代码'''
    response = requests.get(
        url=url,
        headers={
            'User-Agent': choice(agents_list_pc)
        }
    )
    response.encoding = 'utf-8'
    return response.text


def html_to_file(html):
    with open('1.html', 'w',encoding='utf-8') as wf:
        wf.write(html)


def to_mongo(item):
    db =conn.spiderdb
    myset = db.lianjia
    myset.insert(item)


def parse_one_page(html):
    '''解析一个页面的房源信息'''
    def parse_info(info_html):
        pattern = r'<span class="divide">/</span>(.*?)<span class="divide">/</span>(.*?)米<span class="divide">/</span>(.*?)<span class="divide">/</span>.*'
        infos = re.findall(pattern, info_html)
        return infos

    pattern = r'<li class="clear LOGCLICKDATA" >.*?<a class=".*?data-original="(.*?)".*?data-sl="">(.*?)</a>.*?data-el="region">(.*?)</a>(.*?<span class="divide">/</span>.*?<span class="divide">.*?)</div></div><div class="flood">.*?positionInfo">(.*?)<span class="divide">/</span>(.*?)<span class="divide">.*?target="_blank">(.*?)</a>.*?<div.*?class="followInfo">(.*?)<span class="divide">/</span>.*?<div.*?class="totalPrice".*?><span>(.*?)</span>万</div><div class="unitPrice".*?>.*?<div.*?class="unitPrice".*?>.*?<span>(.*?)</span>.*?</li>'
    items = re.findall(pattern, html, flags=re.S)
    for item in items:
        d = {
            'image': item[0],
            'name': item[1],
            'infos': parse_info(item[3]),
            'floor': item[4],
            'place': item[2],
            'focus': item[7],
            'total': item[8],
            'price': item[9],
        }
        print(d)
        # to_mongo(d)
        to_csv(d)

def main():
    for page in range(1, 100):
        url = get_url(page)
        print(url)
        html = get_index_page(url)
        parse_one_page(html)
        print('第%d页完成' % page)


if __name__ == '__main__':
    main()
















