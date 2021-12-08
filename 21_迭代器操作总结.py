# 可迭代对象：1.生成器 2.元组 列表 集合 字典 字符串
# 如何判断一个对象是否可迭代？
from typing import Iterable

list1 = [1, 2, 3, 4]
print(isinstance(list1, Iterable))  # True

print(isinstance('str', Iterable))  # True

set1 = {1, 2, 3, 4}
print(isinstance(set1, Iterable))  # True

dict1 = {'key': 'value', 'name': 'xiaoli'}
print(isinstance(dict1, Iterable))  # True

g = (x + 1 for x in range(10))
print(isinstance(g, Iterable))  # True

print(isinstance(100, Iterable))  # False

"""
迭代是访问集合元素的一种方式，迭代器是一个可以记住遍历的位置的对象；
迭代器对象从集合的第一个元素开始访问，直到所有元素被访问完结束；
迭代器只能往前不能后退；
可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator

可迭代的是不是肯定是迭代器？
生成器是可迭代的，也是迭代器
list是可迭代的，但不是迭代器

# print(next(list1))
# print(next(list1))
# TypeError: 'list' object is not an iterator
"""

'''
list--->迭代器
list1 = iter(list1) # 通过iter()函数，将可迭代的变成了一个迭代器
print(next(list1))  # 1
print(next(list1))  # 2
'''

'''
迭代器分两类：
    生成器--> next()
    可迭代对象通过iter()函数-->迭代器-->next()
'''
