# eval方法会按照Python解释器规则解析某段文本，并将文本转换为代码并执行，该方法仅限单行代码
f="1+2+3/5"
print(eval(f)) # 3.6

f='print("hello eval")'
eval(f) # 相当于直接执行print("hello eval")这段代码

#exec与eval相似，用于执行多行代码，但不能获取返回值(字符串内代码要顶头写，不能有空格)
f2='''
def fun():
    print("hello exec")
    return 123
        
fun()
'''

res=exec(f2)
print("res",res) # None