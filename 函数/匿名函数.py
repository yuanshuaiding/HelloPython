# 匿名函数：没有名字的函数

# 虽然匿名函数没有名字，但也可以使用一个变量接受一个匿名函数，使用是调用该变量方法即可
import math

fun1 = lambda x, y: x * y

ls = list(range(10))
print(ls)
for index, value in enumerate(ls):
    ls[index] = fun1(value, value)

print(ls)


#还可以使用更简洁的方式

ls2 = list(range(10))
print(ls2)

fun2=lambda x:x*x

ls2=list(map(fun2,ls2))
print(ls2)

# 甚至连函数定义也可以省略，而直接使用匿名函数
ls3 = list(range(10))
print(ls3)

print(list(map(lambda x:x*x,ls3)))


#需要注意的是，Python中的匿名表达式只能用于较为简单的场景（一行代码解决计算），最多支持三元表达式
ls4=range(10)
kv=dict()
for index,value in enumerate(ls4):
    kv[index]=value+1
print(kv)

ls4=list(map(lambda x,y:x*y,kv.values(),kv.values()))
print(ls4)

#求2-50之间的素数(只能被1和自身整除的数)
for i in range(2,50):
    j=2
    flag = False
    while j<=math.sqrt(i):
        if(i%j==0):
            flag=True
            break
        j+=1
    if not flag:
        print(i)

