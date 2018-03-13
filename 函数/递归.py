# 把100除以2，直到不能除,并打印中间结果
import sys


def dd(x):
    x = int(x/2)
    print(x)
    if x > 0:
        dd(x)

# 递归默认可以递归1000层，可以使用sys.setrecursionlimit(10000)来修改默认递归层级
dd(100)

print("默认递归层级",sys.getrecursionlimit())


# 递归的返回值,把100除以2，最多除5次,并返回最后的结果
def dd2(x,count):
    print(x,count)
    if count<5:
        return dd2(x/2,count+1)
    else:
        return x
res=dd2(100,1)
print("res=",res)