from functools import reduce

"""
匿名函数：用lambda关键字创建小型匿名函数，得名于省略了用def声明函数的标准步骤
格式：lambda 参数1, 参数2, ...:运算
匿名函数能接受任何数量的参数但只能返回一个表达式的值
"""

s = lambda a, b: a + b
result = s(1, 2)
print(result)  # 3

'''
匿名函数作为参数
'''


def func(x, y, fun):
    print(x, y)
    print(fun)
    s1 = fun(x, y)
    print(s1)


func(1, 2, lambda a, b: a + b)

'''
匿名函数与内置函数的结合使用
'''

list1 = [1, 3, 2, 6, 4]
m = max(list1)
print('列表最大值：', m)  # 6

list2 = [{'a': 1, 'b': 10}, {'a': 2, 'b': 20}, {'a': 3, 'b': 30}, {'a': 4, 'b': 40}]
m = max(list2, key=lambda x: x['a'])
print('列表最大值:', m)  # {'a': 4, 'b': 40}

'''
map
'''

list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = map(lambda x: x + 2, list3)
print(list(result))  # [3, 4, 5, 6, 7, 8, 9, 10, 11]

# # 效果等同于for循环
# for index, value in enumerate(list3):
#     list3[index] = value + 2
#
# print(list3)
s2 = lambda x: x if x % 2 == 0 else x + 1

result = s2(6)
print(result)  # 6
print(s2(7))  # 8

# 对列表中的奇数进行+1操作
result = map(lambda x: x if x % 2 == 0 else x + 1, list3)
print(list(result))  # [2, 2, 4, 4, 6, 6, 8, 8, 10]

# for index, i in enumerate(list3):
#     if i % 2 != 0:
#         list3[index] = i + 1
#
# print(list3)

'''
reduce(): 对列表中的元素进行加减乘除运算的函数
'''

tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)

result = reduce(lambda x, y: x + y, tuple1)
print(result)  # 45

tuple2 = (1,)
result = reduce(lambda x, y: x + y, tuple2, 10)
print(result)  # 11

result = reduce(lambda x, y: x - y, tuple1)
print(result)  # -43

'''
filter()    对列表元素进行筛选
'''
list4 = [11, 3, 4, 55, 66, 43, 3, 2]

result = filter(lambda x: x > 10, list4)
print(list(result))  # [11, 55, 66, 43]
