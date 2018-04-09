ls = list(range(10))
print(ls)

# 现在对每个元素加1

# 普通方法（遍历列表）
for index, a in enumerate(ls):
    ls[index] = a + 1

print(ls)

# 高级方法（map）
ls = list(map(lambda x: x + 1, ls))

print(ls)

# 装逼方法（列表生成式）
ls = [i + 1 for i in ls]

print(ls)

# 列表生成式里可以使用3元运算符(如:把奇数加1)
ls = [i if i % 2 == 0 else i + 1 for i in ls]
print(ls)