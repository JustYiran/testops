# -*- coding: utf-8 -*-
"""
@Time ： 2021/9/7 21:09
@Auth ： Mr.掌心 2929184523
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：请输入模块功能描述
"""
from selenium import webdriver

driver = webdriver.Ie()
driver.get('http://testingedu.com.cn:8000/Home/user/login.html')
#最大化窗口
driver.maximize_window()
#隐式等待
driver.implicitly_wait(10)

#登录
driver.find_element_by_xpath('//*[@id="username"]').send_keys('13800138006')
driver.find_element_by_xpath('//*[@id="password"]').send_keys('123456')
driver.find_element_by_xpath('//*[@id="verify_code"]').send_keys('1111')
driver.find_element_by_xpath('//a[@class="J-login-submit"]').click()


#修改个人信息
# driver.get('http://testingedu.com.cn:8000/Home/User/info.html')
# driver.find_element_by_xpath('//*[@id="preview"]').click()
# driver.find_element_by_xpath('//*[@id="filePicker"]/div[2]/input').send_keys(r"C:\Users\ZX\Desktop\111.jpg")
