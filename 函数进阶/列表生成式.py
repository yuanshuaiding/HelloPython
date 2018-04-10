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

# 列表生成式里可以使用3元运算符(如:把列表里10以内的奇数加1)
ls = [i if i % 2 == 0 else i + 1 for i in ls if i < 10]
print(ls)

# 语法结构:[expr for iter_var in iterable if cond_expr]

# 嵌套使用列表生成式(最前面的for先循环,每循环一次会让后面的循环完整执行一次)
ls = [(x + 1, y + 1, z + 1) for x in range(5) for y in range(3) for z in range(2)]
print(ls)
