# -*- coding: utf-8 -*-
# @Time : 2019/6/12 16:22
# @Author : Quantum-Ran
# @Email : ai.ei.ui@live.cn
# @File : settings.py
# @Software: PyCharm
class Config:
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'
    SECRET_KEY = 'SZL'


class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'


class DevelopmentConfig(Config):
    DEBUG = True


class Testing(Config):
    DEBUG = True
