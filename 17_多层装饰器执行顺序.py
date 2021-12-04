# 装饰器一
def decorate1(func):
    print('--->1 start')

    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print('刷漆')
        print('--->1 end')

    return wrapper


# 装饰器二
def decorate2(func):
    print('--->2 start')

    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print('铺地板')
        print('--->2 end')

    return wrapper


# 此处装饰器自动执行,因为@decorate2后面是@decorate1而不是一个函数,
# 所以暂停decorate2改为执行decorate1(以此类推直到遇见装饰器+函数);
# 执行@decorate1,将house()传递给decorate1(func),decorate1(func)顺序执行,将wrapper()函数返回;
# 因为返回值是一个函数(此处假设为A()),此时满足@decorate2的执行条件,将A()传递给decorate2(func),
# decorate2(func)顺序执行,将wrapper()当做返回值返回给house()函数
@decorate2
@decorate1
def house():
    print('我是毛坯房...')


# 执行house(),装饰后执行decorate2返回的wrapper(),因wrapper()里面调用了传过来的参数函数A(),
# 所以执行A(),A函数中又调用了传过来的参数函数house(),所以执行house(),以此类推顺序执行完毕即可
house()

"""
函数的多层装饰器总结:
    装饰函数时,从近到远装饰;
    函数执行时,从远到近执行装饰器函数
"""
