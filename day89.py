# -- coding: utf-8 --
# Recursive Algorithm to Compute the Square Root
# We have learned that we can use the binary search algorithm to guess the root – 
# which then converges to the answer we are looking for. 
# We can also use the Recursive algorithm to compute the square root.
# day2 day49 我们又其他方法来计算sqrt 今天学习新的方式
# 假设 n = a**2 + b where a**2 是最大的square number that is less or equal to n
# 比如说 150 = 12的平方 + 6


def rSqrt(n, a, EPS = 1e-8):
    b = n - a*a
    x = a + b/a 
    t = x
    while abs(x*x - n) > EPS:
        x = a + b/(a + t)
        t = x
    return x

# This algorithm works for floating numbers as well. 
# This is recursive algorithm however, the implementation is iterative.
print(rSqrt(150, 12))
