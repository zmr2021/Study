"""
前景提要：写代码要遵循开放封闭原则，它规定已经实现的功能代码不允许被修改，但可以扩展；即：
封闭：已实现的功能代码块
开放：对扩展开放
"""


def w1(func):
    def inner():
        func()

    return inner


@w1
def f1():
    print("f1")


"""
Python解释器自上而下解释代码，步骤如下：
1. def w1(func): ==>将w1函数加载到程序
2. @w1

上例中，@w1内部会执行以下操作：
1. 执行w1函数，并将@w1下面的函数作为w1函数的参数,即：@w1等价于 w1(f1),所以内部会去执行：
def inner():
    f1()

return inner
返回的inner代表一个对f1扩展新功能的函数

2. w1的返回值
将执行完的w1的返回值赋值给@w1下面的函数的函数名f1，即将w1的返回值重新赋值给f1
新f1=def inner():
        f1() # 原f1

        return inner    
"""


# 定义一个装饰器
def decorate(func):
    a = 100
    print('wrapper外层打印测试')  # 1

    def wrapper():
        func()  # 4
        print('-----刷漆-----')  # 5
        print('-----铺地板-----', a)  # 6

    print('wrapper加载完成')  # 2
    return wrapper  # 3


# 当python程序执行到这里,就会自动进行装饰,而不是调用的时候才装饰的
@decorate  # house() = decorate(house)
def house():
    print('我是毛坯房')


# 在调用house()前,已经进行装饰了
house()
'''
1. house是被装饰函数
2. 将被装饰函数作为参数传递给装饰器decorate
3. 执行decorate函数
4. 将返回值又赋值给house
'''
