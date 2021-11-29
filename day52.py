# -- coding: utf-8 --
# Pascal Triangle Algorithms and Applications
# 帕斯卡三角形 和 它的应用
# 帕斯卡三角形 张这个样子 我们可以发现 下一列的数是上一列相关的两个数的和 同时 
# 每一列的和 是 2的行次方   每一列组成的数 比如 121 是 11的2次方 其他同理
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]

# 我们可以看出来 p(r,c) = p(r-1, c) + p(r-1, c -1) r是行c是列

# 我们来打印 这个 帕斯卡三角形 

# from functools import lru_cache
# @lru_cache(maxsize=None)
def f(r, c):
    if r == 0 or c == 0 or r == c:
        return 1
    return f(r - 1, c) + f(r - 1, c - 1)
 
# print the first 8 rows of a Pascal Triangle
# 这种思想是我们知道了下面的事上面的计算出来的 我们相当于是 down-to-up 不断递归出来的结果
for r in range(8):
    a = []
    for c in range(r + 1):
        a.append(f(r, c))
    # print(a)

# 这里其实有很多的重复计算 我们可以用notebook来存一下其实

# We can print the first row, and then second row 
# and this goes on printing all other rows of Pascal Triangle. 
# This is a iterative top-down approach:
# 这种思想是 从up到down 计算
def pascal(rows):
    data = [0] * rows
    # print(data)
    for r in range(rows):
        data[0] = 1   # 列0是1
        data[r] = 1   # 行和列相等是是1
        # print(r)
        for c in range(r - 1, 0, -1):
            print("----",c, data)
            data[c] += data[c - 1]
        print(data[:r+1])

pascal(8)