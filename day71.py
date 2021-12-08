# -- coding: utf-8 --
# Compute the Number of Trailing Zeros for Factorial N 
# 计算N的阶乘结果里 有几个0 
# 比如 5的阶乘 5x4x3x2x1 = 120 有一个0

from typing import Counter


def countZero(n):
    factorial = 1
    for i in range(2, n+1):
        factorial *= i
    # 上面计算出阶乘结果
    zeroCount = 0
    while factorial % 10 == 0:
        zeroCount += 1
        factorial //= 10
    return zeroCount

# 时间复杂度 O(N平方) for循环是O(N) 然后下面是基于N不断%10
print(countZero(5))

# 我们可以了解到的是 造成0的 因素是 5和2  那么有几个0 其实就是数有几个 min(5个数，2个数) 明显5个数更少 那么就数5就行了
def countZero2(n):
    zeroCount = 0
    for i in range(5, n+1, 5): #从5开始到n步长5
        while i % 5 == 0: # 因为比如i是25 里面有很多个5
            zeroCount += 1
            i //= 5
    return zeroCount

print(countZero2(5))

def countZero3(n):
    zeroCount = 0
    while n > 0:
        n //= 5
        zeroCount += n
    return zeroCount
print(countZero3(25))