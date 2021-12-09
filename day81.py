# -- coding: utf-8 --
# Compute the Hamming Distance of Two Integers
# 计算两个整数的 hanmming距离差 也就是计算两个整数 二进制表示下 不同位的和 
# 我们知道 异或 两位不同那么得1 那么这个不同为的和就用得到
# 比如 101（5）   1000（8）   他们异或的结果是 1101 这里有三个1 确实他们有三位是不同的
# 然后 day79 又讲了如何计算 二进制的1的个数
def hammingDis(a, b):
    n = a ^ b
    ans = 0
    while n > 0:
        ans += 1
        n = n & (n - 1)
    return ans

print(hammingDis(5, 8))