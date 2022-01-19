# -- coding: utf-8 --
# Maximum Subarray by Dynamic Programming and Greedy Algorithm
# 求最大子数组和的三种算法(暴力、贪心和动态规划)	

# subarray要去连续的子序列 必须得连续

# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Example 2:
# Input: nums = [1]
# Output: 1

# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23

# 暴力法

n = [5,4,-1,7,8]

import math

def maxSubArry(nums):
    ans = -math.inf
    for i in range(len(nums)):
        s = 0
        for j in range(i, len(nums)):  # 两层for一般都这么写 i一层 j从i开始一层 i范围0-n-1 j范围i-n-1
            s += nums[j]  
            ans = max(ans, s)
    return ans
#时间复杂度O(N平方) 
print(maxSubArry(n))

# 动态规划法
def maxSubArry2(nums):
    ans = c = nums[0]
    for i in nums[1:]: #从第二个开始
        c = max(i, c+i)   # 这里就体现了动态规划的思想 我们要么选c+i 就是加上新的 要么就是重新开始选i当做新的subarray的开头
        ans = max(c, ans)  # 因为我们要求最终的和 
    return ans
#时间复杂度O(n) 空间O(1)

# 贪心
def maxSubArry3(nums):
    ans = -math.inf
    s = 0
    for i in nums:
        if s >= 0:
            s += i
        else:
            s  = i
        ans = max(s, ans)
    return ans
# 看上去和动态规划差不多 只不过我们 策略是 如果加上新的数是负数 那么我们就跳过 用新的数当开头 