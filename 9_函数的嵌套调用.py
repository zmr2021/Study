"""
一个函数里面调用另外一个函数，就是所谓的函数嵌套调用
例如：用户登录函数调用验证码函数
"""
import random


def generate_checkcode(n):
    s = '0123456789zxcvbnmlkjhgfdsaqwertyuiopQAZXSWEDCVFRTGBNHYUJMKIOLP'
    code = ''
    for i in range(n):
        ran = random.randint(0, len(s) - 1)
        code += s[ran]
    return code


def login():
    # 验证码
    code = generate_checkcode(5)  # 函数调用
    print('验证码:', code)
    code1 = input('输入验证码:')
    # 验证
    if code.lower() == code1.lower():
        print("登陆成功！")


login()
