"""
元组（tuple）：存储任意类型数据，但其内数据不可变。
特例:元组不可变，其内的列表中的元素可以变
"""
t = (1, 2, 3, True, 'abc')  # 元组内类型任意
print(type(t))  # <class 'tuple'>

t1 = ([1, 2, 3], 4)  # 可以修改列表中的元素
print(id(t1))  # 2366229766592
t1[0].append(4)
print(t1)  # ([1, 2, 3, 4], 4)
print(id(t1))  # 2366229766592
t1[0][2] = 9
print(t1)  # ([1, 2, 9, 4], 4)
print(id(t1))  # 2366229766592

"""
1.定义
"""
t2 = ()  # 空元组的定义
print(type(t2))  # <class 'tuple'>

t2 = ('xzc',)  # 单个内容元组定义[不加逗号为字符串类型]
print(type(t2))  # <class 'tuple'>
t2 = ('xzx')
print(type(t2))  # <class 'str'>

"""
2.索引 切片
"""
users = ('root', 'westos', 'redhat')
passwords = ('123', '456', '012')

print(users[0])  # root
print(type(users[0]))  # <class 'str'>
print(users[:1])  # ('root',)
print(type(users[:1]))  # <class 'tuple'>

"""
3.重复
"""
print(users * 3)  # ('root', 'westos', 'redhat', 'root', 'westos', 'redhat', 'root', 'westos', 'redhat')

"""
4.连接
"""
print(passwords + ('012', '230'))  # ('123', '456', '012', '012', '230')

"""
5.成员操作符
"""
print('redhat' in users)  # True
print('redhat' not in users)  # False

"""
6.循环遍历
"""
for user in users:
    print(user)
# root
# westos
# redhat


"""
7.枚举+迭代: 循环遍历并返回索引值和value
"""
for index, user in enumerate(users):
    print('第%d个用户:%s' % (index + 1, user))

# 第1个用户:root
# 第2个用户:westos
# 第3个用户:redhat

"""
8.枚举+压缩: 先对应压缩在一起,再枚举遍历输出
"""
for user, passwd in zip(users, passwords):
    print(user, ':', passwd)

# root : 123
# westos : 456
# redhat : 012

"""
9.计数
    count()
    index()
"""
t = (1, 2.3, True, 'westos')
print(t.count('westos'))  # 统计出现次数
print(t.index(1))  # 返回元素对应索引值

"""
2.排序
    sort()  元组不能用方法排序
    sorted()    用函数排序
"""
a = (1, 9, 6, 3, 7, 8)
a = sorted(a)
print(a)  # [1, 3, 6, 7, 8, 9]

"""
3.接受多个参数(底层涉及拆装包)
"""
scores = (65, 80, 85, 90, 100)
# 将第一个参数赋值给minscore,最后一个参数赋值给maxscore,其余参数赋值给middlescore
minscore, *middlescore, maxscore = scores
print(minscore)  # 65
print(*middlescore)  # 80 85 90
print(middlescore)  # [80, 85, 90]
print(maxscore)  # 100
