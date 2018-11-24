#encoding: utf-8

import pymongo

# 创建链接对象
conn = pymongo.MongoClient('localhost', 27017)

# 创建库对象， spiderdb为库名
db = conn.spiderdb

# 集合对象, t1是集合的名字
myset = db.t1

# insert
myset.remove({"name":'lucy'})
