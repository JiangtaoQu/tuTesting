# -*- coding: utf-8 -*-
# @Time : 2019/6/11 13:47
# @Author : Quantum-Ran
# @Email : ai.ei.ui@live.cn
# @File : XXX.py
# @Software: PyCharm
from hashlib import md5

salt = bytes(input(), encoding='utf8')
# print(salt)
username = bytes(input().strip(), encoding='utf8')
Brand = bytes(input().strip(), encoding='utf8')
print({'Sign': [username, Brand]})
sss = md5(username)
sss.update(Brand)
sss.update(salt)
print(sss.hexdigest().capitalize())
print(sss.hexdigest().capitalize()[:16])
