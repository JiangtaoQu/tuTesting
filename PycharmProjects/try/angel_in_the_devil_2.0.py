# -*- coding: utf-8 -*-
# @Time : 2019/6/2 20:38
# @Author : Mat
# @Email : mat_wu@163.com
# @File : angel_in_the_devil_2.0.py
# @Software: PyCharm
import time

D = 'Devil'
A = 'Angle'
start = 'You are {}'.format(D)
print(start, end=' ')
time.sleep(1)
while 1:
    _ = A
    sss = 'in the {}'.format(_)
    print(sss, end=' ')
    time.sleep(1)
    _ = (A if 'D' in sss else D)
    print('in the {}'.format(_), end=' ')
    time.sleep(1)
