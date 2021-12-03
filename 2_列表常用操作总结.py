"""
作用：类似其他语言的数组。
数组：数字的组合、字母的组合、字符串的组合
符号：[]
列表序列操作有：索引、切片、修改、追加、插入、删除、扩展、统计、排序（翻转）、获取下标、拷贝
"""
import copy

"""
1.索引 list[i]
    列表的索引序号（又称为下标）
    从左到右索引是从 0 开始，  n-1 为最后一个元素
    从右到左索引是从 -1开始， -n 为最后一个一个元素
"""
animals = ['Dog', 'Cat', 'Monkey', 'Chook', 'Snake']
print(animals[0])  # 'Dog'
print(animals[3])  # 'Chook'
print(animals[-1])  # 'Snake'
print(animals[-3])  # 'Monkey'
type(animals[1])  # <class 'str'>
'注意：通过索引取出的元素类型为 str'

"""
2.切片 list[a:b]
索引只能取出python列表中的一个元素;
此外，python为取多个列表元素提供了强大的切片操作，通过冒号(:)分割的两个索引来实现
注意点：
    切片的索引界限可以利用谚语 “顾头不顾尾” 来记忆，也可以理解为数学中的左闭右开，数学式为： [a, b)
    如果省略分隔符前面的索引值，如list[：b]，则表示为从第一个元素开始索引，数学式为：[0,b)
    如果省略分隔符后面的索引值，如list[a：]，则表示为从a开始索引，索引到最后一个元素结束，
    此时表现为 “顾头又顾尾”，数学式为[a,end]
    如果两个索引值全部省略不写，list[:]，此时表示取整个列表
    列表可以按照某种规则索引元素，如list[first:end:step]，first和end索引与前面的a,b一样，step表示步长，
    此方法常用于循环中
"""
animals = ['Dog', 'Cat', 'Monkey', 'Chook', 'Snake']
print(animals[1:3])  # ['Cat', 'Monkey']
print(animals[3:])  # ['Chook', 'Snake']
print(animals[:3])  # ['Dog', 'Cat', 'Monkey']
print(animals[:])  # 整个列表
print(animals[1:4:2])  # ['Cat', 'Chook']
print(animals[::2])  # ['Dog', 'Monkey', 'Snake']
print(animals[::-1])  # ['Snake', 'Chook', 'Monkey', 'Cat', 'Dog']

"""
3.修改
通过列表的下标将对应的元素进行修改
"""
animals = ['Dog', 'Cat', 'Monkey', 'Chook', 'Snake']
animals[3] = 'Horse'  # 将下标为3的元素修改为 'Horse'
print(animals)  # ['Dog', 'Cat', 'Monkey', 'Horse', 'Snake']

"""
4.添加元素(append,extend,insert)
append(), 在列表末尾追加一个元素
extend(iterable), 将可迭代序列的元素一一追加到列表
insert(i,elem), 将元素添加到指定下标
"""
animals = ['Dog', 'Cat', 'Monkey', 'Chook', 'Snake', 'Ox']
print(animals)  # ['Dog', 'Cat', 'Monkey', 'Chook', 'Snake', 'Ox']

fish = ['freshwater_fish', 'saltwater_fish']  # 鱼（淡水鱼和咸水鱼）
animals.append(fish)  # 将鱼追加到 animals 列表里
print(animals)  # ['Dog', 'Cat', 'Monkey', 'Chook', 'Snake', 'Ox', ['freshwater_fish', 'saltwater_fish']]

# 合并两个列表得到新列表
list1 = [1, 2, 3]
list2 = ['s', 2]
list3 = list1 + list2
print(list3)  # [1, 2, 3, 's', 2]

animals = ['Dog', 'Cat', 'Monkey', 'Chook', 'Snake']
fish = ['freshwater_fish', 'saltwater_fish']
animals.extend(fish)  # 将fish列表中的元素追加到animals列表中，组成一个新的列表
print(animals)  # ['Dog', 'Cat', 'Monkey', 'Chook', 'Snake', 'freshwater_fish', 'saltwater_fish']

"注意特殊情况："
animals = ['Dog', 'Cat', 'Monkey', 'Chook', 'Snake']
animals.extend('fish')  # 如果将单个字符串传递给extend,则会遍历字符串并将每个元素追加到列表
print(animals)  # ['Dog', 'Cat', 'Monkey', 'Chook', 'Snake', 'f', 'i', 's', 'h']

animals = ['Dog', 'Cat', 'Monkey', 'Chook', 'Snake']
animals.insert(3, 'Horse')
print(animals)  # ['Dog', 'Cat', 'Monkey', 'Horse', 'Chook', 'Snake']

fish = ['freshwater_fish', 'saltwater_fish']
animals.insert(-4, fish)
print(animals)  # ['Dog', 'Cat', ['freshwater_fish', 'saltwater_fish'], 'Monkey', 'Horse', 'Chook', 'Snake']

"""
5.查找元素(in,not in,index,count)
in(存在), 如果存在返回True,反之False
not in(不存在), 如果不存在返回True,反之False
index(elem[,start,end]), 查询elem是否在列表当中,start和end为起始和终止下标
count(elem), 统计elem在列表中出现的次数
"""
a = ['x', 'y', 1, 'x', 2, 'x']

if 'x' in a:
    print(True)
else:
    print(False)

print(a.index('x'))  # 0
print(a.index('x', 1))  # 3
print(a.index('x', 4))  # 5

animals = ['Dog', 'Cat', 'Monkey', 'Chook', 'Snake', 'Dog']

print(animals.count('Dog'))  # 2
print(animals.count('Cat'))  # 1
print(animals.count('fish'))  # 0

cat = 'Cat'
print(animals.count(cat))  # 1

"""
6.删除元素(del,pop,remove)
del, 通过下标删除list元素
pop, 采用弹栈原理来删除列表最后一个元素
remove(elem), 删除指定元素
clear, 清除列表中的所有元素
"""
animals = ['Dog', 'Cat', ['freshwater_fish', 'saltwater_fish'], 'Monkey', 'Horse', 'Chook', 'Snake']
del animals[2]
print(animals)  # ['Dog', 'Cat', 'Monkey', 'Horse', 'Chook', 'Snake']

animals.remove('Chook')  # 删除指定元素
print(animals)  # ['Dog', 'Cat', 'Monkey', 'Horse', 'Snake']

animals.pop()  # 删除最后一个元素
print(animals)  # ['Dog', 'Cat', 'Monkey', 'Horse']

animals.clear()  # 删除列表中的所有元素
print(animals)  # []

del animals  # 删除整个列表
# print(animals)  # NameError: name 'animals' is not defined

"""
7.排序和反转(sort,reverse)
sort(self, key=None, reverse=False), 默认从小到大排序,reverse为True则为倒序,可以指定key来选择其他排序
reserve(), 将字符串顺序反转
注意： python3.0不允许不同数据类型进行排序 
同时有数字和字符串的情况，不能排序
"""
aa = [234, 23, 2, 123]

aa.sort()  # 数字从小到大排列
print(aa)  # [2, 23, 123, 234]

aa = [234, 23, 2, 123]
aa.sort(reverse=True)  # 默认从小到大排列，然后转置了
print(aa)  # [234, 123, 23, 2]

# aa.sort(key=len)  # 数字不能用len
# Traceback (most recent call last):
#   File "<pyshell#8>", line 1, in <module>
#     aa.sort(key=len)
# TypeError: object of type 'int' has no len()

"字符串情况： 默认ASCII表先后顺序排列"
a = ['x11', 'abc323', 'e26', '112ddd']

a.sort()  # 默认按照ASCII表先后顺序排序
print(a)  # ['112ddd', 'abc323', 'e26', 'x11']

a.sort(key=len)  # 默认第一原则 字符串从短到长排序，第二原则ASCII表先后顺序
print(a)  # ['e26', 'x11', '112ddd', 'abc323']

a.sort(key=len, reverse=True)
print(a)  # ['112ddd', 'abc323', 'e26', 'x11']

"""
8.拷贝:列表的拷贝分为浅拷贝和深拷贝
浅拷贝(copy):对于多层列表,浅拷贝只为第一层列表内容创建新的地址,内层内容共用同一地址空间
深拷贝(deepcopy):对于多层列表,深拷贝会为每层内容创建新的地址,每层内容彼此独立
"""

list_1 = ['x', 'y', 'z', [1, 2, 3]]  # 创建list_1

list_1_copy = list_1.copy()  # 拷贝list_1
list_1_copy[1] = 'Y'  # 修改第一层元素的值
print(list_1, list_1_copy)  # 修改的第一层位置元素不同
# ['x', 'y', 'z', [1, 2, 3]] ['x', 'Y', 'z', [1, 2, 3]]

list_1_copy[-1].append(4)  # 修改第二层元素的值
print(list_1, list_1_copy)  # 修改的第二层位置元素相同
# ['x', 'y', 'z', [1, 2, 3, 4]] ['x', 'Y', 'z', [1, 2, 3, 4]]

"或者用copy模块的copy方法，同样是浅拷贝："

list_1 = ['x', 'y', 'z', [1, 2, 3]]  # 创建list_1
list_2 = copy.copy(list_1)  # 浅拷贝
list_1[1] = 'Y'  # 改变第一层的值
list_2[-1].append(5)  # 改变第二层的值
print(list_1, list_2)  # ['x', 'Y', 'z', [1, 2, 3, 5]] ['x', 'y', 'z', [1, 2, 3, 5]]

"深拷贝需要用deepcopy方法："

list_1 = ['x', 'y', 'z', [1, 2, 3]]  # 创建list_1
list_3 = copy.deepcopy(list_1)  # 深拷贝
list_1[2] = 'zz'  # 改变第一层的值
list_3[-1][-3] = 888  # 改变第二层的值
print(list_1, list_3)  # ['x', 'y', 'zz', [1, 2, 3]] ['x', 'y', 'z', [888, 2, 3]]

"""
9.常用函数:
max()、min()、sum()
"""
'求列表中的最大值和最小值'

# 假设最大值和最小值
maxvalue = list1[0]
minvalue = list1[0]

for value in list1:
    if value > maxvalue:
        maxvalue = value
    if value < minvalue:
        minvalue = value

print('最大值是：', maxvalue, '最小值是：', minvalue)

# python自带方法
maxvalue = max(list1)
minvalue = min(list1)
print('最大值是：{} 最小值是：{}'.format(maxvalue, minvalue))

'求和'

sum1 = 0
for i in list1:
    sum1 += i
print('列表数和', sum1)

sum1 = sum(list1)
print('自带函数求和：{}'.format(sum1))

"""
10.列表的循环删除问题:
"""
a = [1, 2, 3, 4, 5, 6, 7]

for i in a:
    if i == 3 or i == 4:
        a.remove(i)
print(a)  # [1, 2, 4, 5, 6, 7]
'''
问题产生原因:当i=3时,删除了3后,4会向前补位到3原来的位置,但是循环继续进行,原本i=4变成了i=5,使4跳过了循环
解决办法
'''

b = [1, 2, 3, 4, 5, 6, 7]
c = []

for i in b:
    if i == 3 or i == 4:
        c.append(i)

for i in c:
    b.remove(i)

print(b)  # [1, 2, 5, 6, 7]
