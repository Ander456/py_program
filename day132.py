# -- coding: utf-8 --
# Longest Consecutive Run of 1s in Binary
# 给定一个数 求最长的连续的二进制的1 有多少个 
# 比如 15 1111 结果是4  23 10111 结果是3

# 转化成字符串处理
def f(n):
    b = bin(n)
    bin_str = b[2:] #这一步把前面的0b去掉
    return max(len(x) for x in bin_str.split('0'))

print(f(15))
# 时间复杂度O(logN)

# 用&的方式 求1
def f2(n):
    ans = 0
    c = 0
    while n:
        if n & 1:
            c += 1 #表示最后一位是1
        else:
            c = 0
        ans = max(c, ans)
        n >>= 1
    return ans
print(f2(23))
