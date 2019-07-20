# -*- coding: utf-8 -*-
# @Time : 2019/6/12 16:19
# @Author : Quantum-Ran
# @Email : ai.ei.ui@live.cn
# @File : test.py
# @Software: PyCharm
from flask import session, redirect, url_for
import functools


def auth(func):
    # functools.wraps(func)——把传入的函数，信息还原
    # @functools.wraps(func)
    def inner(*args, **kwargs):
        if not session.get('user'):
            return redirect(url_for('login'))
        ret = func(*args, **kwargs)
        return ret

    return inner


@auth
def index():
    pass


print(index.__name__)
