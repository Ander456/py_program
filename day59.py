# -- coding: utf-8 --
# Re-implement the zip and zip_longest Function in Python
# 实现 python 内置 zip 函数

# 什么是zip ？？ 其实本身英文意思是 拉链拉锁 。。不是压缩 。。 不过你看看那些压缩软件图标也有个拉链 哈哈哈
# 那zip函数是干什么的呢？？ 你把它就想象成拉拉锁把 把两边合并一起 然后不断往上拉 
# a = [1,2,3,4] b = [5,6,7,8,9]
# c = zip(a, b) => [(1,5,), (2,6), (3,7), (4,8)]
# zip_longest(a, b) => [(1,5,), (2,6), (3,7), (4,8), [None, 9]]

def zip(a, b):
    l = min(len(a), len(b))
    for i in range(l):
        yield (a[i], b[i])

def zip_longest(a, b):
    l = max(len(a), len(b))
    for i in range(l):
        aa = None if i >= len(a) else a[i]
        bb = None if i >= len(b) else b[i]
        yield (aa, bb)


a = [1,2,3,4] 
b = [5,6,7,8,9]
print(list(zip(a, b)))

print(list(zip_longest(a, b)))

# day55 也用到了 zip
    