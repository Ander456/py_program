# -- coding: utf-8 --
# Algos of Greatest Common Divisor and Least Common Multiples
# 最大公除数 和 最小公乘数  比如 25 35 最大公除数是5    最小公乘数是 25x35/GCD（最大公除数）
# 数学问题这是 规律

def gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a


print(gcd(35, 25))


def lcm(a,b):
    return a*b/gcd(a,b)


print(lcm(25, 35))