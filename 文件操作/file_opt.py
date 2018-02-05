import chardet
# 一次性读取文件
f = open(file='文本.txt', mode='r', encoding='gb2312')
data = f.read()
print(data)
f.close()


f=open('文本.txt', 'rb')
data=f.read()
print(data)
formate=chardet.detect(data)
print(formate)
f.close()

# 逐行读取
f=open('文本.txt', 'r',encoding='gbk')
for line in f:
    print(line)

# 写
# 如果没有对应文件，则自动创建，否则直接覆盖原文件
f=open('文本1.txt', 'w',encoding='gbk')
f.write("新的文本")
f.close()
# 以二进制点方式写入
f=open('文本2.txt','wb')
f.write('新的文本wb'.encode('gbk'))
f.close()

# 文件末尾追加写入
f=open('文本.txt', 'a',encoding='gbk')
f.write("\n追加新的文本")

# 读写混合操作
f=open('文本.txt', 'r+',encoding='gbk')
data=f.read()
print(data)
f.write("\n追加新的文本r+")
data=f.read()
print("new content",data)
f.close()