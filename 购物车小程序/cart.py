from 函数进阶.迭代器 import fibs

prod = ["mac pro", "mi pad", "iphone"]
# while True:
#     for i in prod:
#         print(i)
#     index = int(input("序号"))
#     print(index)
#     print(prod[index])
#     print("".ljust(30,"-"))

g=fibs(10)
for i in g:
    print(i ,end=" ")
