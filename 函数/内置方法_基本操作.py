a = [1, 2, 3, 4, 5, -1]

print(min(a))

print(max(a))

# all方法只有集合或列表里出现0或False时才会为False，其他均为True,包括空列表
print("all", all(a))
print("all", all([]))

# any与all相反，只要有一个值为True，则返回True,其他情况返回False
print("any", any(a))

# dir打印当前运行程序里的所有变量(包括系统运行时自动创建的变量）
print(dir())

# 如果指定了变量名，则打印该变量的内部变量
print(dir(a))

# 查看当前运行程序里的所有变量及其值（dir()只会查找变量名）
print(vars())

# 获取全局变量集合（类似vars()）
print(globals())

# 打印局部变量
def ff():
    n=3
    print(locals())

ff() # {'n': 3}

# slice 系统内置的切片方法
s = slice(1, 5, 2)  # 从索引1截取到索引5，步长为2
b = a[s]
print(b)  # [2,4]

# sorted 系统内置排序函数，可以指定排序字段即升降
dic = {0: 1, 1: 5, 2: -5, 3: 9, 4: 10}
# 对字段的key按升序排列
ls = sorted(dic.items(), key=lambda x: x[0])
print(ls)
# 对字典的value按降序排列
ls = sorted(dic.items(), key=lambda x: x[1], reverse=True)
print(ls)

# hex 查看某个integer数字的16进制
print(hex(123)) # 0x7b

# oct 查看8进制
print(oct(123)) # 0o173

# bin 查看二进制
print(bin(123)) # 0b1111011

#对字符串进行ascii编码,英文不会被编码
c='abc你好'
print(ascii(c)) # abc\u4f60\u597d

#查看字符串在Ascii码表里的位置
index=ord('a')
print(index) # 97

#获取指定位置的字符
ch=chr(97)
print(ch) # a

#对列表提供索引（从0开始对列表元素编号）
enum=enumerate(a)
print(list(enum))# [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, -1)]

# 列表求和
total=sum(a)
print("total=",total)


# 判断某个变量是否可以调用（是否为函数）
cal=callable(a)
print(cal) # False

def f():
    pass
cal=callable(f)
print(cal) # True

# 获取小数位数(四舍五入)
n=1.234567
print(round(n)) # 1
print(round(n,2)) #1.23
print(round(n,4)) #1.2346