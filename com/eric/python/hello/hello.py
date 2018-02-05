# -*- coding:utf-8 -*-
a='tom'
age=20
name=""
print(a,age)

info='''
-------------------info of %s------------------

name :            %s
age  :            %s
-------------------info end--------------------
''' % (a,a,age)

print(info)

age=20


def judage(age):
    print("开始判断年龄")
    if age>18:
        print("you are adult")
    elif age>14:
        print("you are young")
    else:
        print("you are child")


while age>0:
    judage(age)
    age-=1
else:
    print("年龄判断完成，未出现异常")

