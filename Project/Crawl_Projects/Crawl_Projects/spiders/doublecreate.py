# -*- coding: utf-8 -*-
# @Time : 2019/7/11 16:08
# @Author : Quantum_Ran
# @Email : ai.ei.ui@live.cn
# @File : doublecreate.py
# @Software: PyCharm
from .people import PeopleSpider


class DoubleCreate(PeopleSpider):
    name = 'doublecreate'
    keyword = '双创'
    collection = 'news'
