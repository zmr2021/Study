"""
Python字典是另一种可变容器模型，且可存储任意类型对象，如字符串、数字、元组等其他容器模型。
"""

"""
1.创建字典
字典由键和对应值成对组成。字典也被称作关联数组或哈希表。基本语法如下：

注意：
每个键与值用冒号隔开（:）,每对用逗号分割，整体放在花括号中（{}）。
键必须独一无二，但值则不必。
值可以取任何数据类型，但必须是不可变的，如字符串，数字或元组。
"""
# 定义
dict1 = {}
dict2 = dict()
dict3 = {'ID': '21233', 'name': 'lucky', 'age': 18}

# 列表可以转成字典 前提是：列表中元素要成对出现
dict4 = dict([('name', 'lucky'), ('age', 18)])
print(dict4)  # {'name': 'lucky', 'age': 18}

"""
2.访问字典里面的值
"""
print(dict3['ID'])  # 21233
# 如果访问字典里面没有的键的数据,会报错

'如果我们想访问某个键又不确定有没有该键,可以使用get方法,还可以设置默认值'
print(dict3.get('sex'))  # dict3没有对应键返回值为None
print(dict3.get('sex', '男'))  # 查询不存在的键则返回默认值

"""
3.修改字典
方法:
    新增键值对
    删除/修改已有键值对
"""
dict5 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# 通过key修改对应的值
dict5['Age'] = 8
# 新增键值对修改字典
dict5['School'] = 'DSP School'
print(dict5)  # {'Name': 'Zara', 'Age': 8, 'Class': 'First', 'School': 'DSP School'}

"""
4.删除字典元素
del dict[key]
dict.pop(key[,default]) 存在key时,返回值为此key对应的value
                        不存在key时,则返回默认值
dict.clear()     同列表用法
"""
dict6 = {'张三': 100, '李四': 100, '王五': 90, '赵六': 88}

# del dict[key]
del dict6['李四']
print(dict6)  # {'张三': 100, '王五': 90, '赵六': 88}

# dict.pop(key[,default])  根据key删除字典的键值对，返回值是删除键值对的value
result = dict6.pop('张三')
print(result)  # 100
print(dict6)  # {'王五': 90, '赵六': 88}
# pop默认值是删除时没有找到对应的key,所返回的值
print(dict6.pop('a', '不存在此key'))  # 不存在此key

# dict.popitem()   随机删除字典的键值对（一般是从末尾删除元素）
dict6.popitem()
print(dict6)  # {'王五': 90}

"""
5.字典键的特性
"""
# # 不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如下实例：
# dict7 = {'Name': 'Zara', 'Age': 7, 'Name': 'Man'}
# print(dict7['Name'])    # Man

# 键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行


"""
6.字典内置函数&方法
    内置函数:
        cmp(dict1, dict2)  #比较两个字典元素。
        len(dict)              #计算字典元素个数，即键的总数。
        str(dict)              #输出字典可打印的字符串表示。
        type(variable)     #返回输入的变量类型，如果变量是字典就返回字典类型。   
    内置方法:
        dict.clear()    #删除字典内所有元素
        dict.has_key(key)    #如果键在字典dict里返回true，否则返回false
        dict.setdefault(key, default=None)    #和get()类似, 但如果键不已经存在于字典中，将会添加键并将值设为default
"""
dict7 = {'张三': 100, '李四': 100, '王五': 90, '赵六': 88}

# dict.copy()    #返回一个字典的浅复制
result = dict7.copy()
print(result)  # {'张三': 100, '李四': 100, '王五': 90, '赵六': 88}

# dict.fromkeys(seq[, default])  # 创建一个新字典，以序列seq中元素做字典的键，default为字典所有键对应的初始值
list1 = ['aa', 'bb', 'cc']
dict8 = dict.fromkeys(list1, 0)
print(dict8)  # {'aa': 0, 'bb': 0, 'cc': 0}

# dict.items()    # 遍历字典中的键值对,然后以元组的形式保存在列表中
print(dict7.items())  # dict_items([('张三', 100), ('李四', 100), ('王五', 90), ('赵六', 88)])

# dict.keys()    # 遍历字典中的键,保存到列表中并返回
print(dict7.keys())  # dict_keys(['张三', '李四', '王五', '赵六'])

# dict.values()  # 遍历字典中的值,保存到列表中并返回
print(dict7.values())  # dict_values([100, 100, 90, 88])

# dict.update(dict2)    #把字典dict2的键/值对更新到dict里,存在同名key时,新值覆盖旧值
dict9 = {0: 'tom', 1: 'jack', 2: 'lucy', 3: 'lls'}
dict10 = {3: 'lily', 4: 'ruby'}
dict9.update(dict10)
print(dict9)  # {0: 'tom', 1: 'jack', 2: 'lucy', 3: 'lily', 4: 'ruby'}

# 字典的遍历
for key, value in dict8.items():
    print("key=%s,value=%s" % (key, value))
