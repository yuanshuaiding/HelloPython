age=19

def fun1():
    age=20
    print('fun1',"---->",age)
    # 在函数内部定义的函数叫嵌套函数
    def fun2():
        print('fun2',"---->",age)
        def fun3():
            age=30
            print('fun3', "---->", age)
        fun3()
            

    age=21

    # 调用嵌套函数fun2
    fun2()

    #返回函数名（注意没有括号，有括号代表执行）
    return fun2

f2=fun1()

#f2其实对应的是fun1里的嵌套函数fun2，所以可以执行