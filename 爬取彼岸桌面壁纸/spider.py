#encoding: utf-8

from urllib.request import urlopen, Request
from user_agent import agents_list_pc
from random import choice
import re
import time
from multiprocessing import Process


def image_url_to_file(image_url, filename):
    request = Request(
        url=image_url,
        headers={
            'User-Agent': choice(agents_list_pc)
        }
    )
    response = urlopen(request)
    content = response.read()
    with open('images/'+filename, 'wb') as wf:
        wf.write(content)


def get_image_url_and_filename(url):
    request = Request(
        url=url,
        headers={
            'User-Agent': choice(agents_list_pc)
        }
    )
    response = urlopen(request)
    html = response.read().decode('gbk')
    # 获取图片路径
    pattern = r'<tr><td align="left">\n<a href="(.*)" title=".*"><img.*>\n</table>'
    res = re.search(pattern, html)
    image_url = res.group(1)
    # 获取图片标题
    pattern = r'<title>(.*)</title>'
    res = re.search(pattern, html)
    filename = res.group(1) + '.jpg'
    return image_url, filename


def get_url(page):
    BASE_URL = 'http://www.netbian.com/desk/%d-1920x1080.htm'
    url = BASE_URL % page
    return url


def worker(start_page, end_page):
    for page in range(start_page, end_page):
        try:
            url = get_url(page)
            image_url, filename = get_image_url_and_filename(url)
            image_url_to_file(image_url, filename)
            print('成功%d张' % page)
            time.sleep(0.5)
        except Exception as err:
            print(err, '#'*30, page)
            continue


def main():
    pro1 = Process(target=worker, args=(5000, 10000))
    pro2 = Process(target=worker, args=(10000, 15000))
    pro1.start()
    pro2.start()
    pro1.join()
    pro2.join()



if __name__ == '__main__':
    main()