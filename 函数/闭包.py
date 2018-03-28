def fun_out():
    age=10
    def fun_inner():
        #内层函数引用了外层函数的变量age
        print("age","=",age)
    #把fun_inner函数作为外层函数的返回值（返回fun_inner函数的内存地址）
    return fun_inner
#执行外层函数，并把返回值赋值给变量f，由于f对应的是一个函数内存地址，因而可以执行
f=fun_out()
#fun_out()()

#执行f,即内层函数fun_inner在外层函数外被执行,打印"age = 10"
f()

#由于fun_out函数执行完成后，内层函数被返回，即存在了对该内层函数的引用，而该内层函数又存在对外层函数变量age的引用，所以即使外层函数执行完成后也不会释放相关的局部变量
#以上的现象称为闭包
