def hi():
    print('hello python')


hi()


def hello(words="ooo"):
    print(words)


hello("你好")
hello(123)
hello(None)
hello()


# 默认参数
def regist(name, age, sex, country='中国'):
    print(name, age, sex, country)


regist('zhangsan', 19, 'man')
regist('zhangsan', 19, 'man', '日本')

# 关键参数,此时sex，age就是关键参数，他们并没有按照申明的位置赋值
regist('lisi', sex='female', age=22)


# 这样是不可以的
# regist('lisi',sex='femal',22)#SyntaxError: positional argument follows keyword argument

# 这样也是不可以的
# regist('lisi',22,age=22)#TypeError: regist() got multiple values for argument 'age'


# 元祖形式的非固定参数,*users参数可以传入多个参数值（这多个参数会被打包成元祖）
def alert(msg, *users, time):
    for u in users:
        print(msg, u, time)


# 如果非固定参数不是最后一个参数，则之后的参数需要用关键参数赋值的方式(不然会被users参数获取)
alert('CUP报警了', 'eric', 'tom', time='0808')

# 也可以直接定义一个列表来给users赋值，但要使用*的方式，否则列表会被打包成一个元祖元素
alert("内存不足了", *['eirc', 'tom', 'jim'], time='0809')


# 字典形式的非固定参数，**kargs可以把传入的未在方法里声明的关键字参数打包成字典
def fun(message, **kwargs):
    for k in kwargs:
        print(message, kwargs[k])


# name,age,addr未在fun函数里声明，会被打包成字典并赋值给kwargs参数
fun("你好", name='tom', age=18, addr='new york')

# 同理，可以使用**的方式把一个字典赋值给kwagrs
fun('你好', **{'name': "tom", 'age': 18, 'addr': "new york"})


def regist(name, age, country='中国'):
    print(name, age, country)
    if age > 18:
        return True,name
    else:
        return False


status = regist('tom', 20)
print(status)

#全局变量
name = 'tom'

def change_name():
    # 此处name是函数内声明的局部变量，而不是对外部name的赋值操作
    # global name
    name = 'eric'
    print(name)

change_name() # 此处打印eric

print(name) # 此处打印tom

