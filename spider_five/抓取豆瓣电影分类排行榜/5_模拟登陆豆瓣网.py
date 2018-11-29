#encoding: utf-8

from selenium import webdriver

options = webdriver.ChromeOptions()
# 设置无界面
options.set_headless()
# 设置浏览器的分辨率
options.add_argument('window-size=1900x3000')
driver = webdriver.Chrome(options=options)

driver.get('http://www.douban.com')


driver.find_element_by_id('form_email').send_keys('767852841@qq.com')
driver.find_element_by_id('form_password').send_keys('xx123456')

# 截图
driver.save_screenshot('douban.png')

# captcha-solution: property
captcha = input('请输入验证码：')
driver.find_element_by_id('captcha_field').send_keys(captcha)

# 点击登陆
driver.find_element_by_class_name('bn-submit').click()