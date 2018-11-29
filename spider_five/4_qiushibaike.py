#encoding: utf-8
import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get('http://www.qiushibaike.com/')

# 拿到段子
divs = driver.find_elements_by_class_name('content')
for div in divs:
    print(div.text)

# 点击下一页
driver.find_element_by_class_name('next').click()
