# -- coding: utf-8 --
# Generate Prime Numbers using Sieve of Eratosthenes Algorithms
# 素数生成   素数 智能被1和自身整除的数

# 给定一个数子n返回一列素数小于等于n的
# n ≤ 100,000

# Example 1
# Input
# n = 3
# Output
# [2, 3]

# Example 2
# Input
# n = 10
# Output
# [2, 3, 5, 7]

# Example 3
# Input
# n = 20
# Output
# [2, 3, 5, 7, 11, 13, 17, 19]

from curses.ascii import isprint


def generatePrimeNumbers(n):
    ans = []
    def isPrime(n):
        if n <= 1:
            return False
        if n == 2:
            return True #唯一一个偶数素数
        if n % 2 == 0:
            return False #其他偶数都不是
        i = 3
        while i ** 2 <= n:  # 根号N时间复杂度
            if n % i == 0:
                return False
            i += 2 # 奇数里面找从3开始每次+2
        return True
    for i in range(2, n+2):
        if isPrime(i):
            ans.append(i)
    return ans
#时间复杂度O(N*根号N)

# 方法2 
# We can do better by using Sieve of Eratosthenes Algorithm where we erase non-prime numbers from the list. 
# Every iteration, we erase the multiples of the prime numbers from the list, the remaining ones are prime numbers.
# 每次迭代我们都删除掉 素数的倍数
# 比如[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# 我们给定一个数20 那么我们开始迭代
# i从2开始 2x2 <= 20 2是素数么？是那么j=2+2=4 4<=20所以 4不是个素数 然后 j+=2也就是不断加上素数2这些都不是了 
# i变成3 3x3<=20 3是素数么？ 是那么j=3+3=6 所以6不是素数 balbalbalbal
def generatePrimeNumbers2(n):
    isPrime = [False] * 2 + [True] * (n-1) #[0,1]这俩不是 + 后面假定都是
    i = 2
    while i * i <= n:
        if isPrime[i]:
            j = i + i
            while j <= n:
                isPrime[j] = False
                j += i
        i += 1
    return [x for x in range(1, n+1) if isPrime[x]]
# 时间复杂度O(N) 空间同
