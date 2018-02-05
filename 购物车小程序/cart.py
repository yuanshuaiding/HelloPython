prod = ["mac pro", "mi pad", "iphone"]
while True:
    for i in prod:
        print(i)
    index = int(input("序号"))
    print(index)
    print(prod[index])
    print("".ljust(30,"-"))
