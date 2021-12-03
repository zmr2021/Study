"""
1.字符串截取
"""
import operator

s1 = 'hello'
print(s1[0:3])  # hel
# 截取全部字符串
print(s1[:])  # hello

"""
2.消除空格及特殊符号
s.strip()   消除字符串左右两边的特殊字符（包括'\t', '\n', '\r', ''）
s.strip('0')    消除字符串左右两边的特殊字符（如'0'）,字符串中间的'0'不会删除
lstrip,rstrip 用法与strip类似，分别用于消除左、右的字符
"""
s1 = '000hello00world000'
s1 = s1.strip('0')
print(s1)  # hello00world

# s.strip('12') 等价于 s.strip('21')
s1 = '12hello21'
print(s1.strip('12'))  # hello

"""
3.字符串复制
"""
s1 = 'hello'
s2 = s1  # s2 = 'hello'
# 若指定长度
s3 = s1[0:2]  # s3 = 'he'

"""
4.字符串连接
"""
a1 = 'hello'
a2 = 'world'
a3 = a1 + a2  # a3 = 'helloworld'
# 使用operator模块的concat()
a4 = operator.concat(a1, a2)  # concat 为字符串拼接函数

"""
5.字符串比较
    （1）利用operator模块方法比较，包含的方法有
        lt(a, b)    小于(less than)
        le(a, b)    小于等于(less than or equal to)
        eq(a, b)    等于(equal to)
        ne(a, b)    不等于(not equal to)
        ge(a, b)    大于等于(greater than or equal)
        gt(a, b)    大于(greater than)
    （2）关系运算符比较（<,>,<=,>=,==,!=）
"""
result = operator.eq('abc', 'def')  # 根据ASCII码比较
print(result)  # False
print(operator.gt('abc', 'ab'))  # True

d1 = 'abc'
d2 = 'ab'
print(d1 > d2)  # True
print(d1 == d2)  # False

"""
6.求字符串长度
"""
print(len(d1))  # 3

"""
7.求字符串中最大字符、最小字符
"""
q1 = 'hello'
print(max(q1))  # o
print(min(q1))  # e

"""
8.字符串大小写转换
    upper   转换为大写
    lower   转换为小写
    title   转换为标题（每个单词首字母大写）
    capitalize  首字母大写
    swapcase    大写变小写，小写变大写
"""
w1 = 'hello'
w2 = 'WORLD'
w3 = 'hello world'
w4 = 'HELLO world'
print(w1.upper())  # 'HELLO'
print(w2.lower())  # 'world'
print(w3.title())  # Hello World
print(w3.capitalize())  # Hello world
print(w4.swapcase())  # hello WORLD

"""
9.字符串翻转
"""
e1 = 'hello'
print(e1[::-1])  # olleh

"""
10.分割字符串函数
    partition(sep), 以sep将字符串分割成sep前,sep,sep后三部分
    split(sep[,maxsplit])，以sep分割字符串,maxsplit指定最大分割次数
    rpartition(sep), 用法同上,只是从右边开始查找
    splitlines(), 依据换行符进行分割字符串
"""
r1 = 'hello,world'
print(r1.split(','))  # ['hello', 'world']
r2 = 'hello world itcast and itcastapp'
print(r2.partition('itcast'))  # ('hello world ', 'itcast', ' and itcastapp')
r3 = 'hello \nworld!'
print(r3.splitlines())  # ['hello ', 'world!']

"""
11.字符串序列连接
    join方法：
        语法为str.join(seq)    seq为元素序列
"""
l1 = ['hello', 'world']
l2 = '-'
print(l2.join(l1))  # hello-world   字符串类型

"""
12.字符串内查找
    find方法，检查字符串内是否包含子串str
        语法为：str.find(str[,start,end])   str为要查找子串；start为查找起始位置，默认为0；end为查找终止位置，
        默认为字符串长度,若找到则返回起始位置索引，否则返回-1
    index方法,语法同find方法,区别在于若未找到会报错
"""
z1 = 'today is a fine day'
print(z1.find('is'))  # 6
print(z1.find('is', 7, 10))  # -1

"""
13.字符串内替换
    replace方法，将字符串中的旧串换成新串
        语法为：str.replace(old, new[, max])    old为旧串；new为新串；max可选，为替换次数
"""
print(z1.replace('fine', 'rainy'))  # today is a rainy day

"""
14.判断字符串组成
    主要方法如下：
        isdigit     检测字符串是否只由数字组成
        isalpha     检测字符串是否只由字母组成
        isalnum     检测字符串是否只由数字、字母组成
        islower     检测字符串是否只含有小写字母
        isupper     检测字符串是否只含有大写字母
        isspace     检测字符串是否只含有空格
        istitle     检测字符串是否是标题（每个单词首字母大写）
"""
x1 = 'hello'
print(x1.isupper())  # False
print(x1.islower())  # True

"""
15.字符串的编码和解码:
    编码:encode(encoding='UTF-8',errors='strict')
    解码:decode
"""
x2 = '好好学习!'
xe = x2.encode()
print(xe)  # b'\xe5\xa5\xbd\xe5\xa5\xbd\xe5\xad\xa6\xe4\xb9\xa0!'
print(xe.decode())  # 好好学习!

"""
16.判断字符串开头结尾
判断字符串以xxx开头/结尾,返回值为布尔类型
    startswith()    endswith()
应用:文件上传
"""
filename = '笔记.doc'
if filename.endswith('doc'):
    print('成功上传doc文件!')
else:
    print('请确认文件格式!')
