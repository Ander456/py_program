# -- coding: utf-8 --
# Dynamic Programming Algorithms to Count Numbers of Unique Digits
# 动态规化算法数不重复数字的数
# 我们要计算 n位数 有多少个 位移的 digitis(十进制数字)

# Example:
# Input: 2
# Output: 91
# Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, 
# excluding 11,22,33,44,55,66,77,88,99
# Constraints:
# 0 <= n <= 8

# 我们知道 第一位 可以是1-9 不能是0 那就9种选择 第二位 0-9 减去 第一位这个（因为不能重复）那就又是9 依次 第三位是8 
# 那我们就知道 是 9x9x8x7x...

def count(n):
    if n == 0:
        return 1 
    def f(k): # 计算k位数字 unique十进制数的数量
        ans = 9
        for i in range(1, k):
            ans *= 10 - 1
        return ans
    ans = 10 # f(0) = 1 f(1) = 9 so is 10
    for i in range(2, n+1):
        ans += f(i)
    return ans
print(count(2))
# 时间复杂度O(n*k)
# 但是这里我们引入一个 鸽子和 鸽子笼子的概念 
# 我们有10个鸽子 和11个笼子 我们怎么放鸽子 即使你一个笼子一个 或者一个笼子多个 那么 结果一定会是 至少有一个笼子是空的
# 放到这里 十进制 就10个数  可以选  如果 我们要count的11位数。。。那肯定这11个坑里。。会有 重复的数字。。就不是unique的了
# 所以优化下
def count2(n):
    if n == 0:
        return 1 
    def f(k): # 计算k位数字 unique十进制数的数量
        if k > 10:
            return 0
        ans = 9
        for i in range(1, k):
            ans *= 10 - 1
        return ans
    ans = 10 # f(0) = 1 f(1) = 9 so is 10
    for i in range(2, n+1):
        ans += f(i)
    return ans
print(count2(2))
# 通过上面我们很清楚的知道了 f(n) 和 f(n-1)的关系 
# f(n) = f(n-1) * (11-n)  # n = 2 f(2) = f(1) * (9) 也就是 9 x 9 没问题 

# 动态规划 top-down + memo
#@cahce
def count3(n):
    def f(n):
        if n == 0:
            return 1
        if n == 1:
            return 9
        return f(n-1) * (11-n)
    return sum(f(n) for n in range(0, n+1))
print(count3(2))

# 动态规划 bottom-up
def count4(n):
    dp = [0] * 11 # 为什么定义11位数？ 就是上面讲那个格子 理论
    dp[0] = 1
    dp[1] = 9
    for i in range(2, n+1):
        dp[i] = dp[i-1] * (11 - i)
    return sum(dp[i] for i in range(n+1))
print(count4(2))
