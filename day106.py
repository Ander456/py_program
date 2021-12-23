# -- coding: utf-8 --
# Multipy Two Integers Without Multipy, Division & Bit Shifting

# 不用 乘法 触发 位运算 来 模拟两个数的相乘 

# If a is smaller than b, for example, 3*5, we prefer 5+5+5 instead of 3+3+3+3+3, because the former involves less addition operations. We can implement this in pure recursion:
def mul(a, b):
    if a == 0 or b == 0:
        return 0
    if a < 0 and b < 0:
        return mul(-a, -b)
    if a < 0:
        return mul(-a, b)
    if b < 0:
        return mul(a, -b)
    if a > b:  # 都是正数的情况下 我们更愿意 让数更小的作为迭代次数 数更大的作为基数
        return mul(b, a)
    return mul(a - 1, b) + b  # -1个b相乘 + b才是最终结果  也就是我们用 + 来模拟了乘


def mul2(a, b):
    if a == 0 or b == 0:
        return 0
    if a < 0 and b < 0:
        return mul(-a, -b)
    if a < 0:
        return mul(-a, b)
    if b < 0:
        return mul(a, -b)
    if a > b:
        return mul(b, a)
    ans = 0
    while a > 0:
        ans += b
        a -= 1
    return ans

print(mul(3, 5))
print(mul2(3, 5))