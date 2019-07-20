# -*- coding: utf-8 -*-
# @Time : 2019/6/2 21:32
# @Author : Mat
# @Email : mat_wu@163.com
# @File : angel_in_the_devil_3.0.py
# @Software: PyCharm
import time

D = 'Devil'
A = 'Angle'
start = 'You are {}'.format(D)
print(start, end=' ')
time.sleep(1)
while 1:
    print('in the {}'.format(A), end=' ')
    time.sleep(1)
    print('in the {}'.format(D), end=' ')
    time.sleep(1)
