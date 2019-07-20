# -*- coding: utf-8 -*-
# @Time : 2019/6/2 20:10
# @Author : Mat
# @Email : mat_wu@163.com
# @File : angel_in_the_devil.py
# @Software: PyCharm
import time

count = 0
while 1:
    if count == 0:
        start = 'You are {} in the {}'.format('Devil', 'Angle')
        print(start, end=' ')
        time.sleep(1)
    count += 1
    if count % 2 == 1:
        follow = 'in the {}'.format('Devil')
        print(follow, end=' ')
        time.sleep(1)
    else:
        follow = 'in the {}'.format('Angle')
        print(follow, end=' ')
        time.sleep(1)
