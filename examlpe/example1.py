# -*- coding: utf-8 -*-
"""
@Time ： 2021/9/7 21:01
@Auth ： Mr.掌心 2929184523
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：验证selenium环境
"""
from time import sleep

from selenium import webdriver

#打开浏览器
driver = webdriver.Ie()
#打开被测网站
driver.get('http://www.baidu.com')
driver.find_element_by_xpath('//*[@id="kw"]').send_keys('selenium')
driver.find_element_by_xpath('//*[@id="su"]').click()

sleep(3)
#退出浏览器
driver.quit()