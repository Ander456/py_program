# -- coding: utf-8 --
# Maximum Split Product using Dynamic Programming or Greedy
# 把一个数split开 然后 求乘积最大的

# Constraints
# n ≤ 100,000
# Example 1
# Input
# n = 11
# Output
# 54
# Explanation
# 3 + 3 + 3 + 2 = 11 and 3 * 3 * 3 * 2 = 54

# Hint #1
# What is the least to which you can split the number that gives you the maximum value?

# 方式1 greedy
# The best/optimal strategy is to split into 3 if it can. For example, given 6, 
# the best is to split as 3+3 which has 3*3=9 other than, 2+2+2 (product 8) or 4+2 (product 8), 5+1 (product 5) etc. 
# Thus, we can repeatedly split into 3 – and if it is less or equal 4,
def maxIntergerBrackProduct(n):
    if n == 1 or n == 2:
        return 1
    if n == 3:
        return 2 # 2 1
    ans = 1
    while n > 4:  # 
        ans *= 3
        n -= 3
    return ans * n
# 时间复杂度O(N)

# 方法2 mimomazation 动态规划
# 状态转移方程：f(n) = max(f(n), i * (n-1), i * f(n-1)) 
# 举个例子 比如 f(5) 我们可以split成
#  1     4
#  2     3
#  3     2
#  5     1   
# 同理上面的split是 i (n-i)
# 我们对于 （n-i) 又可以变成递归的f(n-i)


# top-down形式的
def maxIntergerBrackProduct2(n):
    def f(n):
        if n == 1 or n == 2:
            return 1
        ans = 1
        for i in range(1, n):
            ans = max(ans, i * (n-1), i * f(n-1))
        return ans
    return f(n)

# 时间O(N平方) 因为递归里面f(n-1)

# bottom-up形式的
def maxIntergerBrackProduct3(n):
    dp = [1] * (n+1)
    for i in range(1, n+1):
        for j in range(1, i):
            dp[i] = max(dp[i], j*(i-1), j*dp(i-j))
    return dp[-1]

# 时间复杂度O(N平方)