# 语法 from module.xx.xx import xx as rename
# 语法 from module.xx.xx import *(慎用,可能会导致重名冲突)

# 需要注意的是,模块一旦被调用,相当于执行了这个模块里的python文件

# 导入os模块所有功能
import sys

print(sys.path)

import os

dirs = os.scandir()
print(dirs)
hasDirs = False
for i in dirs:
    print(i)
    if isinstance(i, os.DirEntry):
        if 'mydirs' == i.name:
            hasDirs = True

if (not hasDirs):
    os.mkdir('mydirs')  # 在当前文件所在路径创建文件夹mydirs
# 导入django模块的core文件夹下的handlers文件夹里所有的python功能代码
from django.core import handlers

# 导入自定义模块某个功能模块并重命名
from 函数进阶 import 迭代器 as gen

print("\n迭代器模块开始")

for i in gen.fibs(5):
    print(i, end="  ")

print("\n迭代器模块结束")

# 更精准导入自定义某款的某个具体函数(文件里的代码也会执行)
from 函数进阶.生成器 import fib

fib(5)
