# 变量可以指向一个函数定义，而函数的参数能接收变量，即函数参数也可以接收另一个函数为参数，这种可以接收另一个函数为参数的函数称为高阶函数。
# 高阶函数满足以下任意一条即可：
# 1. 接收一个或多个函数为入参
# 2. retrun另一个函数作为返回值
import math

#普通函数
def abc(x):
    return x**2
#普通函数
def bcd(x):
    return math.sqrt(x)

#高阶函数（入参有函数变量）
def calc(x,y,f):
    return f(x)+f(y)

result=calc(5,6,abc)

print(result)

result=calc(4,9,bcd)

print(result)


