#在此处无法直接访问manager模块,因为路径不在一起,跨包了,如何解决此问题?

#方法1:将父级文件夹绝对路径加入到sys.path路径中,这样就可以找到相关包及模块了

import sys

print(sys.path)

BASE_DIR=__file__

import os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(BASE_DIR)))# 向上2级找到父级文件夹

sys.path.append(BASE_DIR)

from ..module2 import manager

def say_hi():
    print("hello from moudule1")

#方法2:使用相对路径

# from ..module3 import setting