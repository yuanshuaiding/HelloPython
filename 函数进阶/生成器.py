##生成器有两种:生成器表达式和生成器函数

##1.下面是一个生成器表达式(注意是小括号)

# 类似于列表推导，但是，生成器返回按需产生结果的一个对象，而不是一次构建一个结果列表
g = (i * i for i in range(10))
print(g)
# 手动调用next函数来获取生成器产生的数据
print(next(g))
# 循环获取生成器产生的值
for i in g:
    print(i, end="  ")  # 0  1  4  9  16  25  36  49  64  81

print()


##2.下面是一个生成器函数(跟普通函数定义一样,由python根据yield推断是否为生成器函数),通过yield返回多个值
def func():
    print('first')
    yield 11111111
    print('second')
    yield 2222222
    print('third')
    yield 33333333
    print('fourth')


g = func()
print(g)
from collections import Iterator

print(isinstance(g, Iterator))  # 判断是否为迭代器对象

# 手动调用next(g)来获取生成的数据
# print(next(g))
# print('======>')
# print(next(g))
# print('======>')
# print(next(g))
# print('======>')
# print(next(g))

# 使用循环表达式获取生成的数据
for i in g:  # i=iter(g)
    print(i)


#######斐波那契数列########
##普通函数实现
def fib(max):
    fls = list()
    n, a, b = 0, 0, 1
    while n < max:
        print(b, end='  ')
        fls.append(b)
        a, b = b, a + b
        n += 1
    print()
    print(fls)


fib(15)


##使用生成器生成斐波那契数列(将推算过程中的结果通过yield返回)
def fib_g(max):
    n, a, b = 0, 0, 1
    while n < max:
        print("fib_g", ":", b, end="|")
        flag = yield b  # 函数执行到此处冻结,并将值返回给next()函数或循环,直到下一次调用next()或循环,函数从此处唤醒并继续执行,依次类推,直至函数完全执行结束或循环结束
        print("flag:", flag)
        if flag == 'stop':
            break  # 此处处理相关逻辑
        a, b = b, a + b
        n += 1


g = fib_g(15)  # 调用生成器函数得到生成器对象

print(g)  # <generator object fib_g at 0x000001BCD6541DB0>

print(g.__next__())  # 1

print(g.send("hi"))  # 1

for i in g:
    if i > 200:
        #g.send('stop')  # 在生成器函数里接收到stop
        # 循环结束,则会停止对生成器的调用,即生成器函数终止
        break
    else:
        print("(", i, ")", sep="", end='--->')
