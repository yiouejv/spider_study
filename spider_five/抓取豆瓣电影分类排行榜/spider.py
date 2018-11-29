#encoding: utf-8
import csv
import json
from datetime import datetime
from time import ctime, time

import requests

from spider_five.抓取豆瓣电影分类排行榜.config import db, db_session
from spider_five.抓取豆瓣电影分类排行榜.models import Movie


def get_json_data(limit=None):
    url = 'https://movie.douban.com/j/chart/top_list?'
    if limit == None:
        limit = input('输入要抓取的电影数量：')
        try:
            limit = int(limit)
        except Exception as err:
            print(err)
    params = {
        'type': 11,
        'interval_id': '100:90',
        'start': 0,
        'limit': limit,
        'action': '',
    }
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'll="108290"; bid=RWBxn8XF_eo; __yadk_uid=qPLXWmnlXHb0l2B0WXGjuyD8U2W5dZ7h; _vwo_uuid_v2=D292BAA54A74858AAA28225C06C9E3ADE|cde0d443e54ae06db2b393cf62952cbe; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1543368658%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utmc=30149280; __utma=223695111.1343023010.1542788457.1542788457.1543368658.2; __utmb=223695111.0.10.1543368658; __utmc=223695111; __utmz=223695111.1543368658.2.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=30149280.50272632.1542788457.1543368658.1543368662.3; __utmz=30149280.1543368662.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmb=30149280.1.10.1543368662; _pk_id.100001.4cf6=39031496386fcb0d.1542788456.2.1543369719.1542788456.',
        'Host': 'movie.douban.com',
        'Referer': 'https://movie.douban.com/typerank?type_name=%E7%88%B1%E6%83%85&type=11&interval_id=100:90&action=',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    res = requests.get(url=url, params=params, headers=headers)
    res.encoding = 'utf-8'
    if res.status_code == 200:
        print('获取json数据成功...')
        return res.text
    else:
        print('请求失败，正在重试...')
        get_json_data(limit)


def parse_json_data(data):
    items = json.loads(data)
    for i, item in enumerate(items, 1):
        movie = {
            'title': item.get('title'),
            'image': item.get('cover_url'),
            'is_playable': item.get('is_playable'),
            'types': item.get('types'),
            'regions': item.get('regions'),
            'release_date': item.get('release_date'),
        }
        # to_mongo(movie)
        # print(i, '条记录存入mongodb成功')
        # to_file(item)
        # print(i, '条数据存入excel成功')
        to_mysql(movie)
        print(i, '条数据存入mysql成功')


def to_mongo(item):
    myset = db.douban
    myset.insert(item)


def to_file(item):
    with open('douban.csv', 'a', newline='', encoding='gbk') as wf:
        writer = csv.writer(wf)
        writer.writerow([value for value in item.values()])


def to_mysql(item):
    movie = Movie(
        title=item['title'],
        image=item['image'],
        is_playable=item['is_playable'],
        types=json.dumps(item['types'], ensure_ascii=False),
        regions=json.dumps(item['regions'], ensure_ascii=False),
        release_date=item['release_date'],
    )
    db_session.add(movie)
    db_session.commit()


def main():
    data = get_json_data()
    parse_json_data(data)


if __name__ == '__main__':
    main()