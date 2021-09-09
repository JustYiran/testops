# -*- coding: utf-8 -*-
"""
@Time ： 2021/9/8 22:06
@Auth ： Mr.掌心 2929184523
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：请输入模块功能描述
"""


# def f1():
#     print("这是函数名字")
#
# f1()
# s = "f1"
# print("%s是个字符串"%s)

class fun:
    def f1(self):
        print("这是函数1")

    def f2(self, a, b):
        print("这是函数2")
        print(a + b)

    def f3(self, c='1', d='2'):
        print("这是函数3")
        print(c + d)

#
f = fun()
input_f = input("输入要执行的函数")
# print(type(input_f))
func = getattr(f, input_f)
input_c = input("输入函数的参数").split(',')
# func(*input_c)

# if input_f == 'f1':
#     f.f1()
# elif input_f == 'f2':
#     f.f2(*input_c)
# elif input_f == 'f3':
#     f.f3(*input_c)
# else:
#     print("函数不存在")
