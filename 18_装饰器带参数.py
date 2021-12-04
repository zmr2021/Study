"""
带参数的装饰器是三层
最外层的函数负责接收装饰器参数
里面的内容是装饰器原内容
"""


def outer(a):  # 第一层，负责接收装饰器的参数
    def decorate(func):  # 第二层，负责接收函数
        def wrapper(*args, **kwargs):  # 第三层，负责接收函数实参/返回值
            ret = func(*args, **kwargs)
            print('---> 铺了{}块地板'.format(a))

            return ret

        return wrapper

    return decorate


# 1.先执行outer(10)函数，这个函数return的结果是decorate这个函数的引用，
# 2.@decorate
# 3.使用@decorate对house进行装饰
@outer(10)
def house(time):
    print('我在{}号拿到的房子，是一个毛坯房...'.format(time))


house('2016-2-2')


@outer(100)
def street():
    print('新修的街道：长寿路')


street()
