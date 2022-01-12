# -- coding: utf-8 --
# Find N Unique Integers Sum up to Zero

# Given an integer n, return any array containing n unique integers such that they add up to 0.

# Example 1:
# Input: n = 5
# Output: [-7,-1,1,3,4]
# Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].

# Example 2:
# Input: n = 3
# Output: [-1,0,1]

# Example 3:
# Input: n = 1
# Output: [0]

# Constraints:
# 1 <= n <= 1000

# Hints:
# Return an array where the values are symmetric. (+x , -x).
# If n is odd, append value 0 in your returned array.

# 其实就是给定一个数n 表示我们最终返回的数组里元素的个数 让我们放n个数这n个数互相都不相同都是唯一的然后 sum是0

# 我们可以从1开始 一对一对的给
def sumZero(n):
    i = 1
    ans = []
    while n >= 2:
        ans.append(i)
        ans.append(-i)
        i += 1
        n -= 2
    if n == 1:
        ans.append(0)
    return ans

# 我们也可以直接从1给到n-1 然后这n-1个数的和是一个数 我们再给一个负数的这个数 
def sumZero2(n):
    i = 1
    s = 0
    ans = []
    while n > 1:
        ans.append(i)
        i += 1
        s += i
        n -= 1
    ans.append(-s)
    return ans
    
