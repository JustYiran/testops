# -*- coding: utf-8 -*-
"""
@Time ： 2021/9/8 22:40
@Auth ： Mr.掌心 2929184523
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：请输入模块功能描述
"""
import os

import pytest

if __name__ == '__main__':
    pytest.main(['-s', './ddt/test_web.py', '--alluredir', './temp'])
    os.system('allure generate ./temp -o ./report --clean')