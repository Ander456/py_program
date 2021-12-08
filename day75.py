# -- coding: utf-8 --
# Algorithms of Power of Two
# # 检测一个数是否是2的幂 和day74 一模一样。。只不过3换成了2
# 所以3能用的方法 换2 就可以了 
# 但是 2有个特殊的 比如 2的二进制10  4的二进制100 8 1000 
# 可以发现如果 n&(n-1) == 0 那么它肯定是 2的幂 

def isPowerOf2(n):
    return n > 0 and (n & n-1) == 0

print(isPowerOf2(1024))
print(isPowerOf2(1))