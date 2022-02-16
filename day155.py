# -- coding: utf-8 --
# Implement the Accumulate Function in Python
# Python的accumulate函数的实现

from itertools import accumulate
a = [1,2,3,4,5]
print(accumulate(a))
print(list(accumulate(a)))

def accumulate(a):
    for i in range(1, len(a)):
        a[i] += a[i-1]
    return a

def accumulate2(a):
    for i in range(1, len(a)):
        a[i] += a[i-1]
    yield from a

# deep copy
def accumulate3(a):
    b = [a[0]]
    for i in range(1, len(a)):
        b.append(a[i] + b[-1])
    yield from b


# 时间复杂度O(N) n是list数量