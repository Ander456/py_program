# -- coding: utf-8 --
# Sum of First N Odd Numbers (with Math Induction)
# 前n个奇数和 

def sumOfOdd(n):
    ans = 0
    for i in range(1, 2*n, 2):  #三个参数分别是start stop step
        ans += i
    return ans

# 前几个奇数 那么比如前5个奇数 我们肯定要算到 2*5 10这个数
# 时间复杂度O(n) 空间复杂度O(1)

def sumOfOdd2(n):
    return n*n

# 一个规律是 前n个奇数和 是n的平方 比如 前1个 那么是 1*1 =1  前两个 = 1+3 = 4 == 2的平方

# 用math induction证明 参靠day17 就是 数学证明
# f(n) = n*n  
# 1. base case  f(1) = 1 == 1* 1
# 2. f(k+1) = f(k) + 2*k+1  也就是k+1个奇数和 是f(k)个奇数和+2*k+1这个 
# 然后 f(k) = k*k 那么 k的平方+2*k+1 也即是k+1的平方 为啥？ 因为(a+b)平方 = a平方+b平方+2ab

print(sumOfOdd(4))

