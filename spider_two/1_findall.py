#encoding: utf-8

import re

html = '''<div><p>仰天大笑出门去</p></div>
<div><p>成也风云，败也风云</p></div>
'''
pattren = r'<div><p>(.*)</p></div>'
lst = re.findall(pattren, html)
print(lst)



#
s = 'A B C D'
p1 = re.compile('\w+\s+\w+')
r1 = p1.findall(s)
print(r1)

# 第一步['A B', 'C D']
# 第二步['A', 'C']
p2 = re.compile('(\w+)\s+\w+')
r2 = p2.findall(s)
print(r2)

# 第一步['A B', 'C D']
# 第二步[('A', 'B'), ('C', 'D')]
p3 = re.compile('(\w+)\s+(\w+)')
r3 = p3.findall(s)
print(r3)


