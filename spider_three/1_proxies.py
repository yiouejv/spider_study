#encoding: utf-8

import requests
from user_agent import agents_list_pc
from random import choice

response = requests.get(
    url='http://www.baidu.com',
    # url = 'http://httpbin.org/get',
    headers={
        'User-Agent': choice(agents_list_pc)
    },
    proxies={
        # 'http': 'http://139.199.38.182:8118',
        'http': 'http://309435365:szayclhp@116.255.162.107:16816',
    }
)

response.encoding = 'utf-8'
html = response.text
print(html)
print(response.status_code)