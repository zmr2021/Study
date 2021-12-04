"""
返回值：将函数中运算的结果通过return扔出来
return 返回值

1. return后面可以是一个参数，接受的时候x = add(1, 2)
2. return后面也可以是多个参数。接受的时候底层会将多个参数放在一个元组中，将元组作为整体返回
3. 接受的时候亦可以是多个:return 'hello', 'word'  x,y=('hello', 'word')
"""


def add(a, b):
    result = a + b
    return result


x = add(2, 3)
print(x)


def func():
    return 'hello', 'world'


hw = func()
print(hw)  # ('hello', 'world')

h, w = func()
print(h, w)  # hello world
