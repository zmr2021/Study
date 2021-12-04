"""
内部函数:在一个函数体中声明的新函数
特点：
    1.可以访问外部函数的变量
    2.内部函数可以修改外部函数可变变量的值
    3.内部函数修改外部函数不可改变的量，需要nonlocal声明
    4.内部函数修改全局不可变变量时，需要使用global声明
"""
s1 = 1000


def func():
    # 局部变量
    n = 100
    list1 = [1, 2, 3, 4]
    global s1

    # 声明内部函数
    def inner_func():
        nonlocal n  # 修改外部函数的不可变量声明
        global s1  # 修改全局变量声明
        for index, i in enumerate(list1):
            list1[index] = i + n  # 修改外部函数的可变变量

        list1.sort()
        n += 1
        s1 += 1

    # 调用内部函数
    inner_func()
    print(list1)
    print(n)
    print(s1)


func()

"""
[101, 102, 103, 104]
101
1001
"""
