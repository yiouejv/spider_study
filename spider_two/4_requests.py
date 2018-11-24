#encoding: utf-8

import requests


response = requests.get('http://www.baidu.com')
# 查看响应编码
print(response.encoding)

# 设置响应编码
response.encoding = 'utf-8'

# 查看响应内容
print(response.text)

# 查看响应内容
print(response.content)

# 查看http响应码
print(response.status_code)

# 返回实际数据的url
print(response.url)
