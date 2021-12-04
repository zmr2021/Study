"""
通用装饰器:
    可以装饰不定长函数和有/无返回值函数的装饰器
"""


def decorate(func):
    def wrapper(*args, **kwargs):  # 接受不定长函数的参数
        print('登陆效验中...')
        print('登陆效验结束')
        ret = func(*args, **kwargs)  # 接受函数的返回值
        return ret

    return wrapper


@decorate  # 装饰无参，无返回值函数
def func1():
    print('-------1-------')


func1()


@decorate  # 装饰有参函数
def func2(s):
    print('-------2-------\n', s)


func2('有参函数')


@decorate  # 装饰有返回值函数
def func3(students, birth='1900'):
    print('{}班级学生如下：'.format(birth))
    for stu in students:
        print(stu)

    return "有返回值函数"


student = ['tom', 'lily', 'pof']
t1 = func3(student)
print(t1)
