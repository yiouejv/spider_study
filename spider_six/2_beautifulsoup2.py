#encoding: utf-8

from bs4 import BeautifulSoup

html = '''<div class="test1">雄霸</div>
<div class="test1">幽若</div>
<div class="test2">
    <span>第二梦</span>
</div>
'''

# 1. 找到所有class为test1的div节点文本

soup = BeautifulSoup(html, 'lxml')
items = soup.find_all('div', attrs={'class': 'test1'})
for item in items:
    text = item.string
    print(text)

# 2. 找到class为test2的div节点下的span文本
items = soup.find_all('div', attrs={'class':'test2'})
for item in items:
    print(item.span.string)
    print(item.children)






