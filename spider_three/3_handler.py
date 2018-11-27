#encoding: utf-8

from urllib import request

# 1. 创建相关的Handler处理器对象
http_handler = request.HTTPHandler()

# 2. 创建自定义opener对象
opener = request.build_opener(http_handler)

# 3. 利用opener对象的open方法发送请求获取响应
url = 'http://www.baidu.com/'
headers = {
    'User-Agent': 'Mozilla/5.0',
}
req = request.Request(url, headers=headers)
res = opener.open(req)
print(res.getcode())