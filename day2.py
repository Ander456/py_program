# -- coding: utf-8 --
# From Linear Search to Binary Search Algorithm
# 求一个数的平方根
def sqrt(n):
    for i in range(n):
        if i * i == n:
            return i


print(sqrt(9))


# 下面这个版本的方法速度更快 使用了二分的思想
def sqrt2(n):
    left, right = 0, n
    while left <= right:
        mid = (left + right) / 2
        if mid * mid == n:
            return mid
        if mid * mid > n:
            right = mid - 1
        else:
            left = mid + 1


print(sqrt(25))
