#encoding: utf-8
import json

jobj = '{"city": "北京"}'
jarray  = '["北京", "上海"]'
print(type(jobj), jobj)
print(type(jarray), jarray)

# 转为python格式
d = json.loads(jobj)
l = json.loads(jarray)
print(type(d), d)
print(type(l), l)

# 转为json格式
jd = json.dumps(d, ensure_ascii=False)
ja = json.dumps(l, ensure_ascii=False)
print(type(jd), jd)
print(type(ja), ja)