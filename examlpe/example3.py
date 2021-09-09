# -*- coding: utf-8 -*-
"""
@Time ： 2021/9/8 20:05
@Auth ： Mr.掌心 2929184523
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：请输入模块功能描述
"""

from examlpe.mywebkeys import Web

web = Web()
web.open_browser('gc')
web.get_url('http://testingedu.com.cn:8000/Home/user/login.html')

#登录
web.input('//*[@id="username"]', '13800138006')
web.input('//*[@id="password"]', '123456')
web.input('//*[@id="verify_code"]', '1111')
web.click('//a[@class="J-login-submit"]')
web.sleep(3)

#修改个人信息
web.get_url('http://testingedu.com.cn:8000/Home/User/info.html')
web.sleep(1)
web.click_js('//*[@id="preview"]')
#进入iframe
web.into_iframe('//*[@id="layui-layer-iframe1"]')
web.input('//*[@id="filePicker"]/div[2]/input', r"C:\Users\ZX\Desktop\111.jpg")
web.click('//div[@class="saveBtn"]')
#切出iframe
web.out_iframe()
web.click('//input[@class="save"]')
web.sleep(3)

#新增地址
web.get_url('http://testingedu.com.cn:8000/Home/User/address_list.html')
web.click('//span[text()="增加新地址"]')
web.input('//input[@name="consignee"]', 'zxtest')
web.input('//input[@name="mobile"]', '17777777777')
web.select('//*[@id="province"]', '湖南省')
web.select('//*[@id="city"]', '25580')
web.select('//*[@id="district"]', '25607')
web.select('//*[@id="twon"]', '岳麓街道')
web.input('//input[@name="address"]', '掌心测试地址')
web.input('//input[@name="zipcode"]', '410000')
web.click('//*[@id="address_submit"]')
web.sleep(3)

#删除地址
web.click('//span[text()="zxtest"]/../..//a[text()="删除"]')
web.sleep(3)

#搜索
web.input('//*[@id="q"]', '手机')
web.click('//*[@id="sourch_form"]/a')

#获取所有商品的名字
goods = web.driver.find_elements_by_xpath('//div[@class="shop-list-splb p"]'
                                         '//div[@class="shop_name2"]/a')
for good in goods:
    print(good.text)

#添加购物车
web.click('//a[contains(text(), "Huawei/华为 nova 2s")]')
web.sleep(3)
web.click('//*[@id="join_cart"]')
web.sleep(1)
web.click('//span[@class="layui-layer-setwin"]/a')
web.move_to('//span[text()="我的购物车"]')
web.sleep(1)
web.click('//a[@class="c-btn"]')
web.sleep(1)

#结算
web.click('//a[text()="去结算"]')
web.sleep(3)
web.click('//button[@class="checkout-submit"]')
web.sleep(3)

#取消订单
web.get_ralation_text('//p[@class="succ-p"]', r'\d{18}')
web.click('//a[text()="我的订单"]')
web.switch_win()
web.sleep(1)
web.click('//em[text()="{text}"]/../..//a[text()="取消订单"]')
web.click('//a[text()="确定"]')
web.sleep(3)


web.quit()