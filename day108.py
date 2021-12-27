# -- coding: utf-8 --
# Longest Increasing Subsequence via Dynamic Programming
# 动态规划算法来求最长递增子序列
# 递增的也就是单调的 最长子序列是可以删除0-n个元素剩下的序列

# 暴力法 我们知道如何求一个数列是否单调 时间复杂度O(N) 然后 所有子序列的数量呢？
# 其实就是 C(n,0) + C(n,1) + ... C(n,n)  = 2的n次方  那么总复杂度O(2的n次方*N) 

# 动态规划 top-down 形式
# 我们定义f(n) 是n个数当前的最长递增子序列长度 
# 状态转移方程 也就是如何让f(n) 和 f(n-1) 建立联系
# f(n) = max(f(n), f(n-1) + 1) 也就是当第n个数大于n-1个数的时候 那么我们可以利用memory已经计算的f(n-1) + 1来得到f(n)

def longestIncSubSeq(nums):
    #@cache
    def f(n):
        ans = 1
        for i in range(n):
            if nums[i] < nums[n]:
                ans = max(ans, f(i) + 1)
        return ans
    return max(f(i) for i in range(len(nums))) 

nums = [10,9,2,5,3,7,101,18]  # 2,3,7,101
print(longestIncSubSeq(nums))

# bottom-up形式
def longestIncSubSeq2(nums):
    n = len(nums)
    dp = [1] * (n+1)
    for i in range(n):
        for j in range(i+1, n):
            if nums[j] > nums[i]:
                dp[j] = max(dp[j], dp[i]+1)
    return max(dp)
# 时间复杂度O(N平方) 
print(longestIncSubSeq2(nums))