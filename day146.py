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

def generatePrimeNumbers2(n):
    isPrime = [False] * 2 + [True] * (n-1) 
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
