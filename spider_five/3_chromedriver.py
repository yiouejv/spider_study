#encoding: utf-8
import time

from selenium import webdriver

# 创建浏览器对象
driver = webdriver.PhantomJS()

# 向百度发请求
driver.get('http://www.baidu.com/')

# 向百度搜索框里发送内容
driver.find_element_by_id('kw').send_keys('美女')

# 点击搜索按钮
driver.find_element_by_id('su').click()

time.sleep(3)
# 截图
driver.save_screenshot('美女.png')

# 关闭浏览器
driver.quit()





