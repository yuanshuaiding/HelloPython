s='当你在穿山越岭的另一边,我在孤独的路上没有尽头'
# 打印字符串
print(s) # 默认会在末尾添加\n

print(s,end='￥') # 会在末尾添加￥

print()

print('tom',18,sep='-->') # 会把多个数据使用-->连接，默认是空格

f=open('内置方法之print.txt','w',encoding='utf-8')

print(s,end='|',file=f)# 把内容写入文件