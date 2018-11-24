#encoding: utf-8

# 网址： 猫眼电影 - 榜单 - top100
# 目标：抓取电影名，主演，上映时间
import csv
import re
import sys
import time
from urllib.request import Request, urlopen
from user_agent import agents_list_pc
from random import choice
import pymongo
from bson import ObjectId
from spider_two.猫眼电影top100榜单.models import Base, session, Movie

def get_url(page):
    BASE_URL = 'http://maoyan.com/board/4?offset=%d'
    try:
        page = int(page)
    except Exception as err:
        sys.exit(err)
    url = BASE_URL % ((page-1)*10)
    return url


def get_html(url):
    request = Request(
        url=url,
        headers={
            'User-Agent': choice(agents_list_pc)
        }
    )
    response = urlopen(request)
    html = response.read().decode()
    return html


def to_mysql(row):
    try:
        movie = Movie(name=row['name'], star=row['star'], time=row['time'])
        session.add(movie)
        session.commit()
    except Exception as err:
        print(err)
        session.rollback()


def save_info(html):
    pattern = r'<div class="board-item-main">.*?<p class="name">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>'
    item_list = re.findall(pattern, html, flags=re.S)
    row = {}
    for item in item_list:
        row['_id'] = ObjectId()
        row['name']= item[0].strip(),
        row['star']= item[1].strip()[3:],
        row['time']= item[2].strip()[5:15],
        to_mongo(row)
        to_mysql(row)
        time.sleep(0.1)


def to_mongo(item):
    conn = pymongo.MongoClient('localhost', 27017)
    db = conn.spiderdb
    myset = db.maoyan
    myset.insert(item)


def main():
    for page in range(1, 11):
        url = get_url(page)
        html = get_html(url)
        save_info(html)
        print('第%d页成功' % page)
    else:
        print('感谢使用')


if __name__ == '__main__':
    main()