# -*- coding: utf-8 -*-
# @Time : 2019/6/12 14:51
# @Author : Quantum-Ran
# @Email : ai.ei.ui@live.cn
# @File : text.py
# @Software: PyCharm
# import re
#
# str1 = 'http://team.com/team?name=a'
# str2 = 'https://team.com/team?name=b'
# str3 = 'http://team.com/sta?name=c'
#
# rc = re.compile(r'http[s]*://team.com/(team|sta)\?name=[abc]{1}')
# print(rc.match(str1).groups())
# print(rc.match(str3).groups())
# print(rc.match(str1))
# print(rc.match(str2))
# print(rc.match(str3))

# datetime——日期和时间的组合。
from datetime import datetime, timedelta, timezone

# 返回当前日期和时间
now = datetime.now()
print(now)
# Struck time→Format string——构建指定日期和时间
dt = datetime(year=2019, month=5, day=20, hour=20, minute=30, second=57, microsecond=48000, tzinfo=None)
print(dt)
# Str→Format string——用户输入的日期和时间是字符串，要处理日期和时间，首先必须把 str 转换为 datetime
print(datetime.strptime('2015-04-19 12:20:00', '%Y-%m-%d %H:%M:%S'))
# Format string→Str——要把它格式化为字符串显示给用户，就需要转换为 str
print(datetime.strftime(now, '%Y-%m-%d %H:%M:%S'))
# Format string→Timestamp
print(dt.timestamp())
# Timestamp→Format string
print(datetime.fromtimestamp(1429417200.0))
# Timedelta——时间差
print(dt + timedelta(days=700))
# 转换时区
dt = datetime(year=2019, month=5, day=20, hour=20, minute=30, second=57, microsecond=48000,
              tzinfo=timezone(timedelta(hours=8)))
print(dt)
