# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束或循环结束。

# 迭代器只能往前不会后退。

# 生成器也是一种特殊的迭代器

#注意可迭代对象和迭代器对象的区别,可迭代对象比如list等，通过iter（list）获得它的迭代器对象，可迭代对象可以重复遍历，迭代器对象由于next（）方法的存在，不可重复遍历）


#使用迭代器对象的方式实现斐波那契数列(指定个数)
class fibs:
    def __init__(self, count):
        self.n = 0
        self.a = 0
        self.b = 1
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        self.n += 1
        if self.n > self.count:
            raise StopIteration
        else:
            return self.a

f=fibs(10)

for i in f:
    print(i,end='  ')