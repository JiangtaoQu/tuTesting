# -*- coding: utf-8 -*-
# @Time : 2019/6/9 16:15
# @Author : Ran
# @Email : ai.ei.ui@live.cn
# @File : mk_exam_dir.py
# @Software: PyCharm
import os
import shutil
import time

current = os.getcwd()
dirname = time.strftime('%Y-%m-%d', time.localtime(time.time())) + ' 李昂'
if os.path.exists(dirname):
    pass
else:
    os.mkdir(dirname)
format_file = ['mp4', 'doc', 'txt', 'exams']
for i in os.listdir(current):
    for ff in format_file:
        if ff in i:
            shutil.move(i, dirname + '\\' + i)
            print(i)
