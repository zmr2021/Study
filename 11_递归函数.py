"""
递归函数：函数自己调用自己

特点：
1. 递归函数必须要设定终点
2. 通常会有个入口
"""


def sum1(n):
    if n == 0:
        return 0
    else:
        return n + sum1(n - 1)


result = sum1(10)
print(result)  # 55
