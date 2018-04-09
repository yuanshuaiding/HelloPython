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

# 文件修改(通过光标定位)
f=open('文本3.txt','w+',encoding='utf-8')
f.write("欢迎光临")
f.flush()
f.seek(6)
f.write('你好')
f.flush()
f.seek(0)
print(f.read())
f.close()

# 文件修改（内存操作）
f=open('文本4.txt','w',encoding='utf-8')
f.write("见到外国人说hello！")
f.flush()
f.close()

f=open('文本4.txt','r+',encoding='utf-8')
data=f.read()

if 'hello' in data:
    data=data.replace('hello','hi')
f.seek(0)
f.truncate()# 清空原文件
f.write(data)
f.close()

# 文件修改（硬盘方式）
f=open('文本5.txt','w',encoding='utf-8')
f.write("见到外国人说hello！\n")
f.write("见到外国人说hello！\n")
f.write("见到外国人说hello！")
f.flush()
f.close()

f_src="文本5.txt"
f_bak='%s.bak' % f_src

f=open(f_src,'r',encoding='utf-8')
f_new=open(f_bak,'w',encoding='utf-8')

for line in f:
    if 'hello' in line:
        line=line.replace('hello','嗨喽')
    f_new.write(line)
f.close()
f_new.close()

import os
os.replace(f_bak,f_src)