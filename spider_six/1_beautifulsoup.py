#encoding: utf-8

from bs4 import BeautifulSoup

html = '<div class="fengyun">雄霸</div>'

# 创建解析对象

soup = BeautifulSoup(html, 'lxml')
res = soup.find_all('div', attrs={
    'class': 'fengyun',
})

# 用get_text() 方法或 string属性获取文本内容
for div in res:
    print(div.get_text())  # 获取文本内容
    print(div.string)
