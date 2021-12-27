# -- coding: utf-8 --
# Dynamic Programming to Compute Least Number of Perfect Squares
# 用动态规划 计算 最少数量的完美Squares 和 

# Given an integer n, return the least number of perfect square numbers that sum to n. 
# A perfect square is an integer that is the square of an integer; in other words,  
# it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

# Example 1:
# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.

# Example 2:
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.

# Constraints:
# 1 <= n <= 10^4

# Greedy approach doesn’t work. For example, 23 is equal to 9 + 9 + 4 + 1 but if you go for greedy which to pick the largest square number less than N, then it will be equal to 16 + 4 + 1 + 1 + 1 which is not optimial.
# 贪心并不总是okay的 比如23 的正解 是 9 9 4 1 这样最少 才4个数    但是如果用担心先找到最大的square 16 那就是 16 4 1 1 1 五个数 

# top-down 形式动态规划 F(N) 表示最少的perfect square 数 to sum up  也就是 F(N) to represent the least number of perfect squares to sum up to N
# 状态转移方程是什么样呢？ F(N) = min(F(N), F(N-j*j) + 1) where j >= 1 and j*j <= N  为什么+1？你减去一个perfect square数 那这时候的总需求数量肯定得 + 1才行啊

# @cache
# def f(n):
#     if n == 0:
#         return 0
#     i = 1
#     ans = float("inf")
#     while i * i <= n:
#         ans = min(ans, f(n-i*i) + 1)
#         i += 1
#     return ans

def f2(n):
    dp = [float("inf")] * (n+1)
    dp[0] = 0
    for i in range(1, n+1):  # O(N)
        j = 1
        while j * j <= n:    # O(根号N)
            dp[i] = min(dp[i], dp[i - j*j] + 1)
            j += 1
    return dp[-1] # or dp[n]

# 时间复杂度O(N*根号N)

print(f2(23))

