# -*- coding: utf-8 -*-
# @Time : 2019/6/12 16:21
# @Author : Quantum-Ran
# @Email : ai.ei.ui@live.cn
# @File : xx.py
# @Software: PyCharm
# import_module——import settings
from importlib import import_module

# 根据这个字段
path = 'settings.Foo'

p, c = path.split('.', maxsplit=1)
m = import_module(p)
cls = getattr(m, c)

for d in dir(cls):
    if d.isupper():
        # 找到静态大写属性
        print(d)
        # 找到其值
        print(getattr(cls, d))
