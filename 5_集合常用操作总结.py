"""
集合中各元素间是无序的，相同元素在集合中唯一存在。
即 集合是无序组合，它没有索引和位置的概念，但可变集合中的元素是可以动态增加或删除的。

应用:
    去重：如列表  去重。
    关系测试：判断数据是否存在 交集，并集，差集  等关系。

集合类型:
    可变集合 —— set
    不可变集合 —— frozenset
"""

set1 = set()  # 创建一个空集合。
list1 = [1.23, "a"]  # 列表类型
dict1 = {1: "a", 2: "b"}  # 字典类型
tuple1 = (1, 2, "b")  # 元组类型
s1 = "厉害了，我的国"  # 字符串

# 将列表，字典，元组，字符串转化为集合
set2 = set(s1)
print(set2)  # {'我', '害', '了', '，', '国', '厉', '的'}

set3 = set(list1)
print(set3)  # {1.23, 'a'}

set4 = set(dict1)
print(set4)  # {1, 2}

set5 = set(tuple1)
print(set5)  # {1, 2, 'b'}

dict2 = {}  # 创建的是字典类型，空字典
set2 = set()  # 创建可变空集合
a = {1, 2, 3, "a"}  # 默认为可变集合
b = set("1,2,3")  # 与a语句等效
c1 = frozenset()  # 创建空的不可变集合，该集合不能添加任何元素。
c2 = frozenset("1,2,3")  # 不可变集合，集合中元素不能增加或删除。

print(type(dict2), type(set2), type(a), type(b), type(c1), type(c2))
# <class 'dict'> <class 'set'> <class 'set'> <class 'set'> <class 'frozenset'> <class 'frozenset'>

f = frozenset(a)  # 将可变集合a转换为不可变集合f
print(f, type(f))  # frozenset({1, 2, 3, 'a'}) <class 'frozenset'>

set3 = set(c2)  # 将不可变集合c2转换为可变集合s1
print(set3, type(set3))  # {'1', ',', '2', '3'} <class 'set'>

"""
1.add()函数
如果集合s中不存在元素x，则将元素x添加到集合s中。
"""
s1 = {1, 2, "a"}
s1.add("ab")  # 将字符串"ab"添加到集合s中
s1.add(1)  # 集合s已存在元素 1 ，但不会报错
s1.add("z")  # 将单字符"z"添加到集合s中
print(s1)  # {1, 2, 'ab', 'a', 'z'}

"""
2.clear()函数
删除集合s中的所有元素。
"""
s1 = {1, 2, 3, "a", "bn"}
s1.clear()  # 删除集合s所有元素
print(s1)  # set()

"""
3.copy()函数
复制生成一个新的集合
"""
s1 = {1, 2, 's'}
s2 = s1.copy()
s1.add(3)
s2.add(0)
# s1和s2不共用同一个内存地址
print(s1)  # {1, 2, 3, 's'}
print(s2)  # {0, 1, 2, 's'}

"""
4.discard(value)函数
移除集合s中的value元素。若value元素存在，则移除，不存在也不报错。
"""
s1 = {1, 2, 3, 4, 5, "a", "ab", "h"}
s1.discard(1)  # 移除元素 1
s1.discard("ab")  # 移除元素 "ab"
s1.discard("hj")  # 移除元素 "hj",但集合s1中不存在元素"hj"
print(s1)  # {2, 3, 4, 5, 'a', 'h'}

"""
5.remove(value)
移除集合s中的value元素。若value元素存在，则移除，不存在则报错(产生KeyError异常)。
用法同discard
"""

"""
6.pop()
随机移除集合s中的一个元素并返回该元素。若集合为空则报错(产生KeyError异常)
"""
s1 = {1, 2, 3, 4, 5, "a", "b"}
print(s1.pop())  # 随机删除一个元素并返回
print(s1)  # {2, 3, 4, 5, 'a', 'b'}

s2 = set()  # 创建一个空集合
# print(s2.pop())  # s2为空集合，程序会报错。

"""
7.isdisjoint()函数
判断两个集合是否包含相同的元素，若没有相同元素则返回 True，否则返回 False。
"""
a = {1, 2, 3, "a"}
b = {"b", "c", "55", "66"}
c = {1, 2, 5, "a"}
print(a.isdisjoint(b))  # 集合a与集合b无相同的元素 返回True
print(a.isdisjoint(c))  # 集合a与集合c有相同的元素，返回False

"""
8.issubset()
判断两个集合是否是子集关系(A⊆B)。即判断集合a中的所有元素是否都包含在集合b中，若都包含在集合b中则返回True，否则返回False
"""
a = {1, 2, 3, "a"}
b = {1, 2, 3, "a", "b", "c"}
c = {1, 2, 3, "b", "h"}
print(a.issubset(b))  # True 集合a是集合b的子集
print(a.issubset(c))  # False 集合a不是集合b的子集

"""
9.issuperset()
判断两个集合是否是超集(父集)。即判断集合b中的所有元素是否都包含在集合a中，若都包含在集合a中则返回True，否则返回False
超集概念：如果一个集合S2中的每一个元素都在集合S1中，且集合S1中可能包含S2中没有的元素，则集合S1就是S2的一个超集，
反过来，S2是S1的子集。 S1是S2的超集，若S1中一定有S2中没有的元素，则S1是S2的真超集，反过来S2是S1的真子集。
"""
a = {1, 2, 3, "a", "b", "c"}
b = {1, 3, "a"}
c = {1, 2, 3, "b", "h"}
d = {1, 2, 3, "a", "b", "c"}
print(a.issuperset(b))  # 集合a是集合b的真超集.
print(a.issuperset(c))  # 集合a不是集合b的超集。
print(a.issuperset(d))  # a是b的超集但不是真超集

"""
10.交并差与对称差集
符号操作：
in      not in
==  判断两个集合内容是否相等
差集  - 类似函数difference()
交集  &  函数intersection
并集  |  函数union()
对称差集 ((set1 | set2的) - (set1 & set2))    ^  函数symmetric_difference()
"""
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1 in set2)  # False
print(set1 not in set2)  # True
print(set1 == set2)  # False

# 差集
set3 = set1 - set2
print(set3)  # {1, 2}
set4 = set2.difference(set1)
print(set4)  # set(4, 5)

# 交集
set5 = set1 & set2
print(set5)  # {3}
set6 = set1.intersection(set2)
print(set6)  # {3}

# 并集
set7 = set1 | set2
print(set7)  # {1, 2, 3, 4, 5}
set8 = set1.union(set2)
print(set8)  # {1, 2, 3, 4, 5}

'''
例子：
有两个列表：
list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [1, 2, 33, 23, 12, 34]
求两个列表的相同元素和不同元素
'''
list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [1, 2, 33, 23, 12, 34]

set1 = set(list1)
set2 = set(list2)

set3 = set1.intersection(set2)
list3 = list(set3)
print('相同元素为：', list3)

# 对称差集
result = (set1 | set2) - (set1 & set2)
print(result)  # {33, 34, 3, 4, 5, 6, 7, 12, 23}

result = set1 ^ set2  # 两个列表不一样的元素 symmetric_difference()
print(result)  # {33, 34, 3, 4, 5, 6, 7, 12, 23}

result = set1.symmetric_difference(set2)
print(result)  # {33, 34, 3, 4, 5, 6, 7, 12, 23}
'''
difference_update()     # 差集并赋值
s1 = s1.difference(s2) == s1.difference_update(s2)
intersection_update()   # 交集并赋值
union_update()  并集并赋值
symmetric_difference_update()   对称差集并赋值
'''
