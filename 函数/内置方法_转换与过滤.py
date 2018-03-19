ls=[1,2,3,4,5]

#对列表里的每个元素进行自乘
mp=map(lambda x:x*x,ls)

print(list(mp))


#过滤列表，只保留奇数
fl=filter(lambda x:x%2!=0,ls)

print(list(fl))

#列表一一对应
ls2=['a','b','c']

zip=zip(ls,ls2)

print(list(zip)) # [(1, 'a'), (2, 'b'), (3, 'c')]