# -*- coding: utf-8 -*-
# @Time : 2019/6/2 22:02
# @Author : Mat
# @Email : mat_wu@163.com
# @File : angle_in_the_devil.4.0.py
# @Software: PyCharm
import time

D = 'Devil'
A = 'Angle'


def sss(D, A):
    start = 'You are {}'.format(D) + ' in the {}'.format(A)
    return start


print(sss(D, A), end=' ')
time.sleep(1)
while 1:
    if A in sss(D, A).split()[-1]:
        print(sss(A, D)[14:], end=' ')
        time.sleep(1)
    else:
        print(sss(D, A)[14:], end=' ')
        time.sleep(1)
