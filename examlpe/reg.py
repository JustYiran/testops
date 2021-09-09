# -*- coding: utf-8 -*-
"""
@Time ： 2021/9/8 21:19
@Auth ： Mr.掌心 2929184523
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：请输入模块功能描述
"""
import re

s = r"订单号：  202109082113324414    |    付款金额（元）：3228.10"

orderid = re.findall('\d{18}', s)
print(orderid)