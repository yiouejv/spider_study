#encoding: utf-8


list = [
    'https://morvanzhou.github.io/tutorials/machine-learning/ML-intro/2-0-ANN-and-NN/',
    'https://morvanzhou.github.io/tutorials/machine-learning/ML-intro/2-1-NN/',
    'https://morvanzhou.github.io/tutorials/machine-learning/ML-intro/2-2-CNN/',
    'https://morvanzhou.github.io/tutorials/machine-learning/ML-intro/2-3-RNN/',
    'https://morvanzhou.github.io/tutorials/machine-learning/ML-intro/2-4-LSTM/',
]

video_url = [
    'https://upos-hz-mirrorks3u.acgvideo.com/upgcxcode/13/29/26102913/26102913-1-16.mp4?e=ig8euxZM2rNcNbu3hbdVtWRB7bKVhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEVEuxTEto8i8o859r1qXg8xNEVE5XREto8GuFGv2U7SuxI72X6fTr859IB_&deadline=1542961906&gen=playurl&nbs=1&oi=610411839&os=ks3u&platform=pc&trid=bd0758951de745248c8d402d1f47ef3d&uipk=5&upsig=ca3099c34c2ceae8eba026c3b8cc4385',
    'https://cn-jszj-dx-v-08.acgvideo.com/upgcxcode/41/29/26102941/26102941-1-15.flv?expires=1542963000&platform=pc&ssig=vyhoz_7FO_9nBJbJHEZSWQ&oi=610411839&nfa=7VMUDqBQpI8VGBbhQ1faUQ==&dynamic=1&hfa=2042946152&hfb=Yjk5ZmZjM2M1YzY4ZjAwYTMzMTIzYmIyNWY4ODJkNWI=&trid=fae83f61faa14bf097c82a05533b295e&nfc=1',
]


from urllib.request import Request, urlopen
from user_agent import agents_list_pc
from random import choice

request = Request(
    url='https://s1.hdslb.com/bfs/static/player/main/html5/player.js?lastModified=2018-11-07T08:53:21.289Z',
    headers={
        'Referer': 'https://www.bilibili.com/video/av15997715',
        'User-Agent': choice(agents_list_pc),
    }
)

response = urlopen(request)
content = response.read()
with open('2.flv', 'wb') as wf:
    wf.write(content)

print('ok')