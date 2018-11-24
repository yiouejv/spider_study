#encoding: utf-8
import csv

for _ in range(10):
    with open('test.csv', 'a', encoding='utf-8') as wf:
        # 初始化写入对象
        writer = csv.writer(wf)
        # 写入对象的writerow 方法写入数据
        writer.writerow(['霸王别姬', '张国荣', '1993'])
