# -*- coding: utf-8 -*-
# @Time : 2019/7/14 19:09
# @Author : Quantum_Ran
# @Email : ai.ei.ui@live.cn
# @File : server_mongodb.py
# @Software: PyCharm
from copy import copy


def format_insert_many(d):
    """
    把
    dict1 = {
    'title': ['!', '@'],
    'date': ['a', 'b', 'c'],
    'num': [1, 2, 3, 4, 5, 6]
    } 类似于这样的数据转换成

    [{'title': '!', 'date': 'a', 'num': 1},
    {'title': '!', 'date': 'a', 'num': 2},
    {'title': '!', 'date': 'a', 'num': 3},
    {'title': '!', 'date': 'a', 'num': 4},
    {'title': '!', 'date': 'a', 'num': 5},
    {'title': '!', 'date': 'a', 'num': 6},
    {'title': '!', 'date': 'b', 'num': 1},
    {'title': '!', 'date': 'b', 'num': 2},
    {'title': '!', 'date': 'b', 'num': 3},
    {'title': '!', 'date': 'b', 'num': 4},
    {'title': '!', 'date': 'b', 'num': 5},
    {'title': '!', 'date': 'b', 'num': 6},
    {'title': '!', 'date': 'c', 'num': 1},
    {'title': '!', 'date': 'c', 'num': 2},
    {'title': '!', 'date': 'c', 'num': 3},
    {'title': '!', 'date': 'c', 'num': 4},
    {'title': '!', 'date': 'c', 'num': 5},
    {'title': '!', 'date': 'c', 'num': 6},
    {'title': '@', 'date': 'a', 'num': 1},
    {'title': '@', 'date': 'a', 'num': 2},
    {'title': '@', 'date': 'a', 'num': 3},
    {'title': '@', 'date': 'a', 'num': 4},
    {'title': '@', 'date': 'a', 'num': 5},
    {'title': '@', 'date': 'a', 'num': 6},
    {'title': '@', 'date': 'b', 'num': 1},
    {'title': '@', 'date': 'b', 'num': 2},
    {'title': '@', 'date': 'b', 'num': 3},
    {'title': '@', 'date': 'b', 'num': 4},
    {'title': '@', 'date': 'b', 'num': 5},
    {'title': '@', 'date': 'b', 'num': 6},
    {'title': '@', 'date': 'c', 'num': 1},
    {'title': '@', 'date': 'c', 'num': 2},
    {'title': '@', 'date': 'c', 'num': 3},
    {'title': '@', 'date': 'c', 'num': 4},
    {'title': '@', 'date': 'c', 'num': 5},
    {'title': '@', 'date': 'c', 'num': 6}
    ] 这样的格式
    """

    dict_list = []
    """
    先转成这样便于循环
    [[{'title': '!'}, {'title': '@'}], 
    [{'date': 'a'}, {'date': 'b'}, {'date': 'c'}], 
    [{'num': 1}, {'num': 2}, {'num': 3}, {'num': 4}, {'num': 5}, {'num': 6}]]
    """
    for k in d:
        dict_list.append([{k: v} for v in d[k]])

    if len(dict_list) >= 2:
        # 循环次数，比列表长度少一次。
        for i in range(len(dict_list[:]) - 1):
            dict_list1 = []
            for ii_0 in dict_list[0]:
                for ii_1 in dict_list[1]:
                    # 只去前两项，进行 update 操作
                    ii_0.update(ii_1)
                    # 存入列表时 copy 因为 字典不可 hash
                    dict_list1.append(copy(ii_0))
            dict_list[:2] = [dict_list1]
    return dict_list[0]
