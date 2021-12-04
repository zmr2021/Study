"""
函数定义时小括号中的参数，用来接收参数用，称为“形参”；
函数调用时小括号中的参数，用来给函数传递参数，称为“实参”
"""

'''1.无参函数'''


def add1():
    a = 11
    b = 22
    c = a + b
    print(c)


add1()  # 33

'''2.普通参数函数'''


def add2(a, b):
    c = a + b
    print(c)


add2(11, 22)  # 33

'''
3.缺省参数函数
带有默认值的参数一定要位于参数列表的最后面，否则会报出SyntaxError
'''


def print_info(name, age=20):
    print("name=%s,age=%d" % (name, age))


print_info('miki')  # name=miki,age=20
print_info('miki', age=18)  # name=miki,age=18

'''
4.不定长参数
有时可能需要一个函数处理比当初声明时更多的参数，这些参数叫做不定长参数，声明时不会命名

def func_name(*args, **kwargs):
    """不定长参数函数"""
    pass

args为元组，加了(*)的args会存放所有未命名的变量参数；
kwargs为字典，加了(**)的kwargs会存放命名参数，即形如：key=value的参数
'''


def fun(a, b, *args, **kwargs):
    """不定长参数演示"""
    print(a)
    print(b)
    print('args =', args)
    print('kwargs:')
    for key, value in kwargs.items():
        print(key, '=', value)


fun(1, 2, 3, 4, 5, m=6, n=7, p=8)
'''
1
2
args = (3, 4, 5)
kwargs:
m = 6
n = 7
p = 8
'''
c = (3, 4, 5)
d = {'m': 6, 'n': 7, 'p': 8}
fun(1, 2, *c, **d)  # 注意元组和字典的传递方式
'''
1
2
args = (3, 4, 5)
kwargs:
m = 6
n = 7
p = 8
'''
fun(1, 2, c, d)  # 注意不加*与上面的区别
'''
1
2
args = ((3, 4, 5), {'m': 6, 'n': 7, 'p': 8})
kwargs:
'''

'''
5.函数参数的传递方式
Python函数中，对于不可变类型变量可以理解为值传递；对于可变类型变量可以理解为引用传递，本质为对象的传递
'''


# 不可变类型


def foo(num):
    num = 2
    print(num)


a = 1
foo(a)  # 2
print(a)  # 1
'''
在上面代码中，变量a指向1，调用函数foo时，相当于给参数num赋值num=1，这时两个变量都指向1，在foo函数中重新赋值为2后，此时num指向2，a不变'''


def bar(list_1):
    list_1.append(1)


b = []
print(b)  # []
print(id(b))  # 2390866063232
bar(b)
print(b)  # [1]
print(id(b))  # 2390866063232
'''调用函数执行append方法前，b和list_1都指向同一个对象，执行append时，既没有重新赋值操作也没有绑定新的对象，append只是对列表对象插入一个元素，对象没有改变，只是对象的内容改变了；因为b和list_1
指向同一个对象，执行b.append或者list_1.append本质上是对同一个对象进行操作，因此在调用函数后，b的内容发生了变化，但是id（内存中地址）没有改变 '''
