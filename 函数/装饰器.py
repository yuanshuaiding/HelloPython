valided=False

# 无参数的装饰函数
def valid(func):
    def decorate(*args,**kwargs):
        global valided
        if not valided :
            u=input("用户名：")
            p=input("密  码：")
            if u=="eric" and p=="123":
                valided=True
            else:
                print("你无法访问相关功能",func)

        if valided:
            func(*args,**kwargs)

    return decorate

# 带参数的装饰函数
def valid2(area):
    print("进入装饰器函数valid2")
    def decorate_out(func):
        def decorate_in(*args,**kwargs):
            global valided
            if not valided:
                u = input("用户名：")
                p = input("密  码：")
                if u == "eric" and p == "123":
                    valided = True
                else:
                    print("你无法访问相关功能", func)

            if valided:
                func(*args, **kwargs)
                if area !=None:
                    print('当前区域属于',area)
        return decorate_in
    return decorate_out

@valid
def beijing():
    print("欢迎您来".rjust(12,'-').ljust(20,"-"),"beijing")

@valid2('玄武区')
def nanjing(district):
    print("进入南京")
    print("欢迎您来".rjust(12,'-').ljust(20,"-"),"nanjing",district)

@valid
def suzhou():
    print("欢迎您来".rjust(12,'-').ljust(20,"-"),"suzhou")

def hangzhou():
    print("欢迎您来".rjust(12,'-').ljust(20,"-"),"hangzhou")

#遵守程序设计的“开放。封闭原则（源代码不许修改，但可以拓展），对方法增加认证功能


#beijing=valid(beijing)#可以直接使用@valid注解的方式达到同样效果

#suzhou=valid(suzhou)

beijing()

suzhou()

nanjing('孝陵卫')