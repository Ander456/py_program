# -- coding: utf-8 --
# Compute Longest Palindromic Subsequence by Dynamic Programming
# 计算给定字符串里的最长回文串 （可以删掉任意字母 但是不能跟换顺序）

# 我们当然可以暴露try比如给定 n个字符长度的字符串 我们从1到n遍历 拿到所有的子串
# 然后判断这个子串是否是回文串 day8 双指针法可以知道 检测是否回文 时间复杂度O(N)
# 然后 所有子串 C(N,0) + C(N,1) + ... C(N, N) 是2的n次方 那么时间复杂度总是O(2的n次方*n) 很大的复杂度

# 我们用动态规划来做 
 

def f(s, a, b):
    if a > b: #a左边界 b右边界
        return 0
    if a == b:
        return 1
    if s[a] == s[b]:
        return f(s, a+1, b-1) + 2
    # 如果现在边界俩值不等那么只有两种情况
    return max(f(s, a+1, b), f(s, a, b-1))

s = "bbbab"
# print(f(s, 0 , len(s)-1))
# 上面没有用notebook 加速 python里 可以直接在函数上加@cache 会自动帮忙保存计算结果

# 上面是 dp形式的 up-bottom形式 也就是 我们想求left-right之间的 那么我们先求left+1，right-1之间的 直到最小解

# 另一种形式死 bottom-up的
# 问题是 最长回文串 那么我们就定义 dp[n][n] 是n到n字符之间的最长回文串
# 为什么是二维的？因为影响这个结果的两个因素是 两个边界

def f2(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n-1, -1, -1):  # 左边界
        dp[i][i] = 1
        for j in range(i+1, n): # 右边界
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    return dp[0][-1]
print(f2(s))
# 时间复杂度O(N平方) 空间同