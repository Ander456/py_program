# -- coding: utf-8 --
# Ugly Number Detection Algorithm
# 检测一个数是否是丑数 参考day84 检测是否是happy number
# an integer n, return whether its prime factors only include 2, 3 or 5.
# 也就是 一个数是 2**a + 3**b + 5**c 那么这个数就是ugly number  比如 25 它是5的平方 a=0 b=0 c=2

def isUglyNumber(n):
    if n < 0:
        return False
    # 我们不断的让它除以2,3,5
    while n % 2 == 0:
        n //= 2
    while n % 3 == 0:
        n //= 3
    while n % 5 == 0:
        n //= 5
    return n == 1

print(isUglyNumber(25))
print(isUglyNumber(49))


def isUglyNumber2(n):
    if n < 0:
        return False
    for x in [2, 3, 5]:
        while n % x == 0 and n > 1:
            n //= x
    return n == 1

print(isUglyNumber2(25))
print(isUglyNumber2(49))