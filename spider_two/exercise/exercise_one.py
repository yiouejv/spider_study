#encoding: utf-8

html = '''
<div class="animal">
    <p class="name">
        <a title="tigers"></a>
    </p>
    <p class="contents">
        Two tigers two tigers run fast
    </p>
</div>

<div class="animal">
    <p class="name">
        <a title="rabbit"></a>
    </p>
    <p class="contents">
        Small white rabbit white and white
    </p>
</div>
'''

# 第一步：
#     [("tiger", "Two tigers .."), ("rabbit", "Small rabbit...")]
# 第二步：
#     动物名称：tiger
#     动物描述：Two tigers
import re

pattern = r'<div.*?<a title="(.*?)"></a>.*?<p class="contents">\n(.*?)</p>\n</div>'
lst = re.findall(pattern, html, flags=re.S)
print(lst)

for am in lst:
    print("动物名称：%s, 动物描述：%s" % (am[0], am[1].strip()))
