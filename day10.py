# Two Algorithms to Compute Inverse Factorials
# 翻转阶乘 比如 给定一个结果 求是哪个数的阶乘得到的这个数
# 比如 6 -> 3  10->-1


def solve(a):
    if a == 1:
        return 1
    if a <= 0 :
        return -1
    i = 2
    while a > 1:
        if a % i != 0:
            return -1
        a /= i
        i += 1
    return i - 1


print(solve(6))


def solve2(a):
    if a == 1:
        return 1
    if a <= 0 :
        return -1
    s = 1
    i = 2
    while s < a:
        s *= i
        i += 1
    return i - 1 if s == a else -1


print(solve(24))