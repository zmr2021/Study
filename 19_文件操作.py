"""
在Python中，使用open函数可以打开一个已经存在的文件或者创建一个新的文件
open(路径/文件名, 访问模式)

访问模式    说明
    r       以只读方式打开文件（默认模式），文件的指针将会放在文件的开头
    w       写文件，如果该文件已存在则将其覆盖，不存在则创建新文件
    a       打开文件并追加，如果该文件已存在，新内容将会追加到原文件结尾，不存在则创建
    rb      以二进制格式打开一个文件用于只读
    wb      以二进制格式打开一个文件用于写入
    ab      以二进制格式打开一个文件用于追加
    r+      打开一个文件用于读写
    w+      打开一个文件用于读写
    a+      打开一个文件用于追加，如果文件不存在则创建新文件并进行读写
    rb+     以二进制格式打开一个文件用于读写
    wb+     以二进制格式打开一个文件用于读写
    ab+     以二进制格式打开一个文件用于追加，如果文件不存在则创建新文件并进行读写

打开的文件操作完毕要调用close()函数关闭
"""
f = open(r'./test.txt', 'w')
f.close()

"""
1.写数据(write)
write(内容)   每次都会清空文件再写当前内容
writeline(iterable) 没有换行效果
writelines(['赌神高进\n', '赌侠小刀\n', '赌圣周星驰\n']) -->自己加换行
"""
f = open(r'./test.txt', 'w')
f.write('hello world!')
f.close()

"""
2.读数据(read)
read() 读取所有内容
readline() 每次读取一行内容
readlines() 读取所有行保存到列表中
readable() 判断是否可读
"""
f = open(r'./test.txt', 'r')
content = f.read()
print(content)  # hello world!

"""
3.with结合open使用，可以自动释放资源
"""
with open(r'./test.txt', 'r') as stream:
    content = stream.readlines()
print(content)

"""
4.获取当前读写的位置:tell()
"""
f = open(r'./test.txt', 'r')
content = f.read(2)
print(content)

# 查找当前的位置
position = f.tell()
print("当前文件位置:", position)

content = f.read(3)
print(content)
position = f.tell()
print("当前文件位置:", position)
f.close()

"""
5.读写文件时，想从某个位置操作时，可以使用seek()
seek(offset,from)
    offset:偏移量。
  -如果是文本文件
      -需满足以下条件：from=0时，offset>=0；from=1或2时，offset必须为0；
      -若其中含有中文字符，注意from=0时，指针不要对一个中文字符的二进制编码（包含3个偏移量）中间，否则报错。
          一般较难确定正确的位置，所以建议直接设置为0
  -如果是对二进制文件，需满足以下条件：
      -from=0时，offset>=0；
      -from=1，offset可任意（不要超过总文件的范围）；
      -from=2，offset<=0（不要超过总文件的范围）；
from:方向
  0:表示文件开头
  1:表示当前位置
  2:表示文件末尾

"""
f = open(r'./test.txt', 'r')
content = f.read(2)
position = f.tell()
print("当前位置为:", position)

# 设置位置:离文件开头，5字节处
f.seek(5, 0)

position = f.tell()
print("现在位置为:", position)

# 设置位置：离文件末尾，3字节处
f.seek(0, 2)
position = f.tell()
print("现在位置为:", position)

f.close()


"""
6.文件重命名
os模块的rename(旧文件名,新文件名)
"""

"""
7.删除文件
os模块的remove(待删除文件名)
"""

"""
8.文件夹相关操作
1>创建文件夹：os.mkdir()
2>获取当前目录: os.getcwd()
3>改变默认目录：os.chdir()
4>获取目录列表：os.listdir()
5>删除文件夹：os.rmdir()
"""
