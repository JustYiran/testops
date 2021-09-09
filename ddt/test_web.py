# -*- coding: utf-8 -*-
"""
@Time ： 2021/9/8 22:16
@Auth ： Mr.掌心 2929184523
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：请输入模块功能描述
"""
import allure
import pytest
import yaml
from keywords.mywebkeys import Web

f = open('./lib/testcases/testcases.yaml', mode='r', encoding='utf-8')
cases_dict = yaml.safe_load(f)
#print(cases_dict)

@allure.feature('电商测试项目-Chrome')
class Test_Web:
    @allure.step
    def run_step(self, func, value):
        func(*value)

    def run_case(self, POCases):
        allure.dynamic.title(POCases['title'])
        allure.dynamic.description(POCases['des'])
        #获取测试用例步骤
        cases = POCases['cases']
        try:
            for case in cases:
                func = self.web.__getattribute__(case['method'])
                #获取参数
                caselist = list(case.values())
                with allure.step(case['name']):
                    #反射执行
                    self.run_step(func, caselist[2:])
        except Exception as e:
            allure.attach(self.web.driver.get_screenshot_as_png(), '用例报错图', allure.attachment_type.PNG)
            #认为用例是失败的
            pytest.fail('用例执行报错')
        allure.attach(self.web.driver.get_screenshot_as_png(), '用例结果图', allure.attachment_type.PNG)

    def setup_class(self):
        self.web = Web()
        self.web.open_browser()

    @allure.story('登录')
    @pytest.mark.parametrize('POCases', cases_dict['loginPage'])
    def test_login(self, POCases):
        self.run_case(POCases)

    @pytest.mark.parametrize('POCases', cases_dict['searchPage'])
    def test_search(self, POCases):
        self.run_case(POCases)

    def teardown_class(self):
        self.web.quit()