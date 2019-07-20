# -*- coding: utf-8 -*-
# @Time : 2019/6/21 20:53
# @Author : Quantum-Ran
# @Email : ai.ei.ui@live.cn
# @File : myTag.py
# @Software: PyCharm
from django import template

register = template.Library()


@register.simple_tag()
def st(*args, **kwargs):
    print(args, kwargs)
    return
