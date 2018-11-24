#encoding: utf-8

import requests
from user_agent import agents_list_pc

wd = input('请输入搜索内容：')

res = requests.get(
    url='https://www.baidu.com/s?',
    params={
        'wd': wd,
    },
    headers={
        'User-Agent': agents_list_pc[0],
    }
)
res.encoding = 'utf-8'
print(res.text)

with open('1.html', 'w', encoding='utf-8') as f:
    f.write(res.text)