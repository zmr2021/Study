"""
闭包条件：
    1.外部函数中定义了内部函数
    2.外部函数有返回值
    3.返回值是内部函数名
    4.内部函数引用了外部函数的变量
"""


def test(num):
    # 在函数内部再定义一个函数，并且这个函数用到了外部函数的变量，那么将这个函数及用到的一些变量称为闭包
    def test_in(num_in):
        print("in test_in func, num_in is %d" % num_in)
        return num + num_in

    # 其实这里返回的就是闭包的结果
    return test_in


# 给test函数赋值，将20传递给num
ret = test(20)

# 注意这里的100其实传递给了num_in
print(ret(100))
"""
in test_in func, num_in is 100
120
"""

"""
保存返回闭包时的状态（外层函数变量）;
由于没有及时释放外部函数的变量，消耗内存
"""


def test2(a, b):
    c = 10

    def test2_in():
        s = a + b + c
        print(s)

    return test2_in


func1 = test2(6, 9)
func2 = test2(2, 8)

func1()  # 25
func2()  # 20

"""
闭包看似优化了变量，原来需要类对象完成的工作，闭包也可以完成
"""


def test3(a, b):
    def test3_in(x):
        y = a * x + b
        print(y)

    return test3_in


line1 = test3(1, 2)
line1(1)  # 4

line2 = test3(3, 4)
line2(1)  # 7

"""
闭包的缺点：
    1.作用域没有那么直观
    2.因为变量不会被垃圾回收所以有一定的内存占用问题

闭包的优点：
    1.可以使用同级的作用域
    2.读取其他元素的内部变量
    3.延长作用域

闭包总结：
    1.闭包看似优化了变量，原来需要类对象完成的工作，闭包也可以完成
    2.由于闭包引用了外部函数的局部变量，则外部函数的局部变量没有及时释放，消耗内存
    3.闭包使得代码变得简洁，便于阅读代码
    4.闭包是理解装饰器的基础

"""
