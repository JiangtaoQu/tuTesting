# -*- coding: utf-8 -*-
# @Time    : 2019/4/23 11:11
# @Author  : ran
# @Email   : ai.ei.ui@live.cn
# @File    : Transfer video.py
# @Software: PyCharm
import os
import shutil
import time
import re

listdir1 = os.listdir(os.getcwd())
listdir1.remove('Transfer video.py')
ret1 = list(map(lambda x: os.getcwd() + '\\' + x, listdir1))
# print(ret1)
dgl_dir = '德古拉聂云单' + time.strftime('%Y%m%d')
for i in ret1:
    if '昂' in i:
        if os.path.exists(dgl_dir):
            pass
        else:
            os.mkdir(dgl_dir)
        shutil.move(i, os.getcwd() + '\\' + dgl_dir)
    if 'exam' in i:
        if os.path.isdir(i):
            shutil.move(i, os.getcwd() + '\\' + dgl_dir + '\\exam')
        else:
            shutil.move(i, os.getcwd() + '\\' + dgl_dir)
dirname = time.strftime('%Y%m%d') + '第八组'
if os.path.exists(dirname):
    pass
else:
    os.mkdir(dirname)
listdir2 = os.listdir(os.getcwd())
listdir2.remove('Transfer video.py')
ret2 = list(map(lambda x: os.getcwd() + '\\' + x, listdir2))
# print(ret2)
for j in ret2:
    shutil.move(j, os.getcwd() + '\\' + dirname)
