#encoding: utf-8
import re
from random import choice

import pymysql
import requests
from user_agent import agents_list_pc

url = 'http://code.tarena.com.cn'

def get_index_html(url):
    res = requests.get(
        url=url,
        headers={
            'User-Agent': choice(agents_list_pc),
        },
        auth=('tarenacode', 'code_2013'),
    )
    return res.text


def to_mysql(item):
    db = pymysql.connect(
        'localhost',
        'root',
        '123456',
        'spiderdb',
    )
    cur = db.cursor()
    sql = 'insert into tarena(link) values ("%s");' % item

    print(sql)
    cur.execute(sql)
    db.commit()


def parse_one_parse(html):
    pattern = r'<a.*?href=.*?>(.*?)</a>'
    items = re.findall(pattern, html, re.S)
    for item in items[1:]:
        to_mysql(item[:-1].replace('\\', ''))


def main():
    html = get_index_html(url)
    parse_one_parse(html)


if __name__ == '__main__':
    main()
