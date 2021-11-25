# -- coding: utf-8 --
# Pythagorean Theorem and Algorithm to Find Pythagorean Numbers
# 勾股定理  给定一个c 求出 a 和 b     a平方 + b平方 = c平方 直角三角形勾股定理

# 用数学方法验证勾股定理 就是用四个直角三角形 拼成一个 中间有个小矩形的 大矩形
# 然后 四个三角形面积+小矩形面积 = 大矩形面积 就证明了 勾股定理

# 怎么求呢？我们就从让a从1一直试 我们知道c 然后尝试a=一个值 那么我们就能求出b 根据勾股定理 
# 然后我们开方它取整 如果还能 乘方回去 那自然就是这个数

from math import sqrt

def f(c):
    a = 1
    while c * c > a * a:
        b2 = c * c - a * a
        b = int(sqrt(b2))
        if b * b == b2:
            print(a,b,c)
        a += 1

print(f(5))
