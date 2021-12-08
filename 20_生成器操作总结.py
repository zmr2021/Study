"""
通过列表生成式（列表推导式），我们可以创建一个列表；
但是，受到内存限制，列表的容量肯定是有限的；
而且，创建一个包含100万个元素的列表，不仅占用很大的内存空间；
如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了；
所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
这样就不必创建完整的list，从而节省大量的空间；
在Python中，这样一边循环一边计算的机制，称为生成器：generator
"""
"""
得到生成器的方式：
1.通过列表推导式得到生成器
2.通过函数得到生成器
"""

# 1.列表得到生成器
g = (x * 3 for x in range(2))
print(g)  # <generator object <genexpr> at 0x0000018E73EC5B30>

"""生成器有两种调用方式"""
# 方式一：通过调用__next__()
print(g.__next__())  # 0

# 方式二：next(生成器对象)    built-in
print(next(g))  # 3

# """当超出次数调用生成器会报错"""
# print(next(g))  # Traceback (most recent call last):


print('-' * 30)


# 2.借助函数创建生成器
# 只要函数中声明了yield关键字，就说明该函数变成了生成器

def func(digit):
    num = 0
    for i in range(digit):
        print('---1---')
        num += 5
        yield num  # return num + 暂停
        print('---2---')


# print(func())   <generator object func at 0x000002A53713F3C0>
fun = func(5)
print(fun.__next__())  # 函数只会执行到yield num处，然后return num 并暂停程序
print(fun.__next__())  # 再次执行生成器，将会继续执行yield之后的程序到再次遇见yield返回并暂停程序

print('-' * 30)


# 斐波那切数列
def fib(length):
    a, b = 0, 1
    num = 0
    while num < length:
        yield b
        a, b = b, a + b
        num += 1

    return '没有更多元素了'


gen = fib(5)

# 生成器对象可以使用for循环，并且在超出使用次数后会自动结束，而不像next()调用超出次数报错

for n in gen:
    print(n)

# 在循环中，发现拿不到generator的return语句的返回值，如果想要拿到返回值，必须捕获StopIteration错误


g = fib(5)
while True:
    try:
        x = next(g)
        print("value:%d" % x)
    except StopIteration as e:
        print("生成器返回值：{}".format(e))
        break

"""
生成器方法：
    __next__()  获取下一个元素
    send(value) 向每次生成器调用中传值 注意：第一次调用必须是空值

"""


def gen():
    i = 0
    while i < 5:
        temp = yield i  # 第一次执行generator时，yield i 相当于return i + 暂停函数执行
        print(temp)  # 第二次执行generator时，从函数暂停处开始执行，temp并没有赋值（yield i只是返回i并暂停，
        i += 1  # 并不是给temp赋值），因此print(temp)输出为None，程序继续执行并在yield i 处暂停
    return '没有更多了'


g = gen()
print(g.__next__())  # 0
print(g.__next__())  # None 1
# send(value)方法，可以将value当做yield i并赋值给temp（不影响yield i原本的作用）
print(g.send("haha"))  # haha 2
print(g.send("lala"))  # lala 3
