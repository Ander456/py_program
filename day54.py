# -- coding: utf-8 --
# Logarithm Algorithm to Compute the Power x^n Function
# 幂函数的Log(N)求解算法  也就是我们自己实现一个 pow(x, n)

def pow(x, n):
    if x == 0:
        return 0
    if n == 0 or x == 1:
        return 1
    if x < 0:
        x ,n = 1/x, -n
    ans = 1
    for i in range(n): # 让x乘n次那么for循环n次
        ans = ans * x
    return ans
# 时间复杂度O(n)
print(pow(2, 3))

def pow2(x, n):
    if x == 0:
        return 0
    if n == 0 or x == 1:
        return 1
    if x < 0:
        x ,n = 1/x, -n
    if n & 1: # 如果与上1还不为0那么表明n是一个奇数
        return x * pow2(x, n - 1)
    y = pow2(x, n//2)  # 如果是偶数那么我们不断的除以2 就可以时间O(log(N))的时间复杂度  其实原来就是2的8次方 变成了2的4次然后再平方 同理2的4次也可以变成2的2次然后再平方  2^4 = 4^2 because 2^(2^2) = (2^2)^2. 
    # 这里依然是递归思想 不要陷进去 我们递归返回的是我们想要的也就是一个数然后我们拿这个数平方 就达到了目的  每一次递归 都是 如此 
    return y * y

def pow2_1(x, n):
    if x == 0:
        return 0
    if n == 0 or x == 1:
        return 1
    if x < 0:
        x ,n = 1/x, -n
    ans = 1
    while n >= 1:
        if n & 1:
            ans *= x
        x *= x
        n >>= 1 #这个和除以2一样
    return ans

def pow3(x, n):
    return x ** n


# print(pow2(2, 10))
print(pow2_1(2, 10))