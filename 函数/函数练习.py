# 员工管理程序,1.登录，2.选定员工，3.修改员工信息，4.3次登录失败退出程序
emloyes_str = '''Eric,123456,18,Beijing,Android
Tomy,abcdef,19,Nanjing,IOS
Angle,000000,20,Suzhou,Web'''

# 解析字符串，变成列表
employe_list = emloyes_str.split('\n')
print(employe_list)

# 继续解析，变成嵌套列表
for index, em in enumerate(employe_list):
    # print(index,em)
    employe_list[index] = em.split(',')

#print(employe_list)

# 登录系统
loginCount = 0


def login(u, p):
    for em in employe_list:
        if u == em[0] and p == em[1]:
            return True
    return False


def sucess():
    #打印当前员工
    show_employs()


    #输入要修改的员工序号
    while True:
        index = input("选择q退出系统，或选择序号修改员工信息：")
        if (index.isdigit()):
            index = int(index)
        if('q'==index):
            # 退出
            print("系统已退出")
            break
        else:
            select_employ(index);


def show_employs():
    for index,em in enumerate(employe_list):
        print(index,em)

def select_employ(position):
    for index,em in enumerate(employe_list):
        if index==position:
            print(index,em)
            while True:
                index=input("请输入要修改的栏位（从0到4）,或q退出修改：")
                if(index.isdigit()):
                    index=int(index)
                if('q'==index):
                    break
                else:
                    print("当前值为：",em[index])
                    new_value=input("请输入新值：")
                    em[index]=new_value
                    print(em)

while loginCount < 3:

    u = input("用户名：")
    print(u)
    p = input("密  码：")
    print(p)
    valid=login(u, p)
    if valid:
        sucess()
        break
    else:
        loginCount += 1

else:
    #没有break，说明登录失败
    print("非法登录，已退出系统")