# -- coding: utf-8 --
# Algorithms to Check Integer Power of Three
# 检测一个数是否是3的幂 
# 27 就是  9 也是  但是8 不是  1也是 因为3的0次方是1

# 递归
def isPowerOfThree(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    return n % 3 == 0 and isPowerOfThree(n//3)
# 时间复杂度O(log3(N))
print(isPowerOfThree(27))
print(isPowerOfThree(8))

# 非递归
def isPowerOfThree2(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    while n % 3 == 0:
        n //= 3
    return n == 1

# 上面从大除到小 我们当然也可以从小乘到大
def isPowerOfThree3(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    x = 1
    while x < n:
        x *= 3
    return x == n

# 数学公式法 log以c为底的b / log以c为底的a = log以a为底的b
# def isPowerOfThree4(n):
#     if n <= 0:
#         return False
#     if n == 1:
#         return True
#     x = log2(n)/log2(3) # 因为x可能是整数也可能是小数 所以 我们取整 
#     return int(x) == ceil(x) # int()向下取整 ceil向上取整 

# 这种单调的因为从1到n啊肯定是 我们记得monotic单调的都可以用 二分来加速查找
def isPowerOfThree5(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    l, r = 0, n
    while l <= r:
        mid = (l + r) /2
        if mid * 3 == n:
            return True
        elif mid * 3 > n:
            r -= 1
        else:
            l += 1
    return False
# 时间复杂度O(logN的平方) 二分法就是O(logN) 然后mid*3也是logN
print(isPowerOfThree5(27))
print(isPowerOfThree5(8))