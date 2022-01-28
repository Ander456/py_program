# -- coding: utf-8 --
# Combination Sum Up to Target (Unique Numbers) by DP Algorithms
# 无限(unbounded)背包问题之动态规划算法

# Given an array of distinct integers nums and a target integer target, 
# return the number of possible combinations that add up to target. The answer is guaranteed to fit in a 32-bit integer.

# Example 1:
# Input: nums = [1,2,3], target = 4
# Output: 7
# Explanation:
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# Note that different sequences are counted as different combinations.

# Example 2:
# Input: nums = [9], target = 3
# Output: 0

# Constraints:
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 1000
# All the elements of nums are unique.
# 1 <= target <= 1000

# Follow up: What if negative numbers are allowed in the given array? 
# How does it change the problem? What limitation we need to add to the question to allow negative numbers?
# 0和负数都不行会造成无限多个 所以只能是 postive number

# 回溯方法
def combinationSumToTarget(nums, target):
    ans = 0
    def dfs(left, T):
        nonlocal ans
        if T == 0: #表明塞满了背包
            ans += 1
            return
        for i in range(len(nums)): # 每一次我们的选择都可以是 0-len(nums) 标准的dfs回溯  上面是终止条件 这里是选择  下面是递归和回溯
            if T >= nums[i]: #如果当前背包还能放下
                dfs(i, T - nums[i])
    dfs(0, target)
    return ans

# 动态规划
# 我们要求f(n) 表示空间为n的时候的选择item的方法数 比如 f(4) 表示可容纳4的背包可以选择的方法数 
# 这里有点像爬楼梯 我们要爬n 然后每次可以1或者2 那么我们第n阶时候的方法数就可以 f(n) = f(n-1) + f(n-2)来求出方法数
# 这里的话是 比如我们f(4) 然后items=[1,2,3] 那么最后可以放f(4-1)+f(4-2)+f(4-3)
from functools import cache
def combinationSumToTarget2(nums, target):
    @cache
    def f(n):
        if n == 0:
            return 1
        if n < 0 :
            return 0
        ans = 0
        for i in range(nums): # 因为最后一次我们可以的选择从1到len(nums)的
            ans += f(n-i)
        return ans
    return f(target)
# 时间复杂度O(T*len(nums))

# bottom-up形式的dp
def combinationSumToTarget3(nums, target):
    n = len(nums)
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(1, target+1):
        for j in nums:
            if i >= j: # 这里i遍历的背包空间 从1到目标 所以i要>=j才能放进去
                dp[i] += dp[i-j]
    return dp[-1]

