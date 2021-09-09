# -*- coding: utf-8 -*-
"""
@Time ： 2021/9/7 21:36
@Auth ： Mr.掌心 2929184523
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：封装常用方法
"""
import re
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


class Web:

    def __init__(self):
        # 当前运行的浏览器的类型
        self.br = 'gc'
        # 运行自动化的驱动对象
        self.driver: webdriver.Chrome
        self.relations = {}

    def open_browser(self, browser='gc'):
        """
        打开浏览器
        :param browser:
        :return:
        """
        if browser == 'gc' or browser == '':
            self.br = 'gc'
            self.driver = webdriver.Chrome()
        elif browser == 'ff':
            self.br = 'ff'
            self.driver = webdriver.Firefox()
        elif browser == 'ie':
            self.br = 'ie'
            self.driver = webdriver.Ie()
        else:
            self.br = 'gc'
            print("浏览器类型不支持，默认使用谷歌")
            self.driver = webdriver.Chrome()

        self.driver.maximize_window()
        self.driver.implicitly_wait(15)

    def __find_ele(self, locator: str = ''):
        """
        统一定为方式
        :param locator: 元素定位器，同时能够支持id和xpath以及css
        :return:定位到的元素，如果没有就返回None
        """
        if locator is None or locator == '':
            return None
        elif locator.startswith('/'):
            return self.driver.find_element_by_xpath(locator)
        elif locator.startswith('#') or locator.__contains__('>'):
            return self.driver.find_element_by_css_selector(locator)
        else:
            # 默认用id定位
            return self.driver.find_element_by_id(locator)

    def click(self, locator):
        """
        点击元素
        :param locator: 元素定位器
        :return:
        """
        locator = self.__get_relations(locator)
        ele = self.__find_ele(locator)
        ele.click()

    def input(self, locator, value):
        """
        文本输入
        :param locator: 元素定位器
        :param value: 需要输入的文本内容
        :return:
        """
        ele = self.__find_ele(locator)
        ele.send_keys(value)

    def get_url(self, url):
        """
        打开被测网站
        :param url: 需要打开的网站
        :return:
        """
        self.driver.get(url)

    def click_js(self, locator):
        """
        通过js点击
        :param locator:
        :return:
        """
        ele = self.__find_ele(locator)
        self.driver.execute_script("arguments[0].click()", ele)

    def sleep(self, t: str = '0.5'):
        """
        固定等待
        :param t: 需要等待的时间
        :return:
        """
        t = float(t)
        sleep(t)

    def get_title(self):
        """获取网页的标题"""
        title = self.driver.title
        print(title)

    def get_text(self, locator):
        """获取元素的文本"""
        ele = self.__find_ele(locator)
        text = ele.text
        print(text)

    def quit(self):
        self.driver.quit()

    def into_iframe(self, locator):
        """进入iframe"""
        ele = self.__find_ele(locator)
        self.driver.switch_to.frame(ele)

    def out_iframe(self):
        self.driver.switch_to.default_content()

    def select(self, locator, value):
        ele = self.__find_ele(locator)
        select = Select(ele)
        try:
            int(value)
            select.select_by_value(value)
        except:
            select.select_by_visible_text(value)

    def move_to(self, locator):
        ele = self.__find_ele(locator)
        action = ActionChains(self.driver)
        action.move_to_element(ele).perform()

    def get_ralation_text(self, locator, reg):
        """
        获取要关联的文本并且保存为全局变量
        :param locator:
        :param reg: 获取文本的正则表达式
        :return:
        """
        ele = self.__find_ele(locator)
        text = ele.text
        if reg:
            text = re.findall(reg, text)[0]
        self.relations['text'] = text
        print(text)
        print(self.relations)

    def __get_relations(self, params: str = ''):
        """
        获取关联
        :param params: 需要关联的参数
        :return: 返回关联后的字符串
        """
        if params:
            for key in self.relations:
                params = params.replace('{' + key + '}', str(self.relations.get(key)))
        return params

    def switch_win(self):
        handles = self.driver.window_handles
        print(handles)
        self.driver.close()
        self.driver.switch_to.window(handles[1])








