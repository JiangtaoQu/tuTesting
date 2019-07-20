# # [1,2,3,4] 生成不重复数字的 3 位数
# from itertools import product
#
# list1 = [1, 2, 3, 4]
# for f, s, t in product(list1, list1, list1):
#     if all([f != s, s != t, t != f]):
#         print(f, s, t)
#
# from itertools import islice
#
# for i in islice(range(10), 1, 8, 3):
#     print(i)

# set1 = set()
# # print(set1)
# set1 = set((1, 2, 3, 4, 3, 2, 4, 6, 4))
# set1.add('1')
# print(set1)
