# -- coding: utf-8 --
# Dynamic Programming to Count Number of Palindrome Substrings
# 动态规化算法数回文子字符串

# Example 1:
# Input: “abc”
# Output: 3
# Explanation: Three palindromic strings: “a”, “b”, “c”.

# Example 2:
# Input: “aaa”
# Output: 6
# Explanation: Six palindromic strings: “a”, “a”, “a”, “aa”, “aa”, “aaa”.

# 暴力法 我们先找到所有的子串 然后判断这个子串是否是 回文的
def f(s):
    n = len(s)
    ans = 0
    for i in range(n):  # i 范围 0-n-1
        for j in range(i, n):  # j 范围 i-n-1
            a = s[i:j+1] # 子串
            if a == a[::-1]: # [::-1]reverse
                ans += 1
    return ans
# 时间复杂度O(N的3次方）
print(f("aaa"))

# 动态规划 top-down
# 状态转移方程 f(i,j) 表示在i-j这之间s是否是回文子串
# f(i,j) = s[i] == s[j] and f(i+1, j-1) #如果i-j之间是那么抛去i和j之间也同一样肯定是回文子串
def f2(s):
    def f(i, j):
        if i > j:
            return True
        return s[i] == s[j] and f(i+1, j-1)
    n = len(s)
    # return [f(i, j) for i in range(n) for j in range(i, n)].count(True)
    ans = 0
    for i in range(n):
        for j in range(i, n):
            if f(i,j):
                ans += 1
    return ans # 这一块就等于上面这一行
# 时间复杂度O(N平方)
print(f2("aaa"))

# 动态规划 bottom-up
def f3(s):
    n = len(s)
    dp = [[True] * n for _ in range(n)] # 二维数组
    for i in range(n-1,-1,-1): # 倒着走
        for j in range(i+1, n): # j在i右边
            dp[i][j] = s[i] == s[j] and dp[i+1][j-1]
    return [dp[i][j] for i in range(n) for j in range(i, n)].count(True)
# 时间复杂度O(N平方) 空间复杂度O(N平方）
print(f3("aaa"))
