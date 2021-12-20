# -- coding: utf-8 --
# Climbing the Stairs using Dynamic Programming Algorithm
# 爬楼梯 每次只能爬 1jie或者2jie 爬到顶 一共有多少种爬法

# 这种 问多少种法的 不是 bfs|dfs  就是动态规划 一般 

# 和day99一样 我们爬到顶 怎么爬到顶？ 从倒数第二或者第三都可以 一次爬到 ，这种倒着推的方法backward 很好
def f(n, nb = {}):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n in nb:
        return nb[n]
    val = f(n-1) + f(n-2)
    nb[n] = val
    return val

print(f(4))

# @lru_cache(maxsize=None)
# def f2(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     return f2(n-1) + f2(n-2)
# print(f2(4))

# 上面这种方法是 up-bottom 也就是 我们要求f(n) 需要f(n-1) 和f(n-2)然后不断往下 找到最小的解

# 我们依然可以 bottom-up 拿到最小的解然后不断往上走
def f3(n):
    a, b = 1, 1 #最小的 爬到第一节阶梯的方法数 只有1 
    for _ in range(1, n):
        a, b = b, a + b  # 因为符合斐波那契的算法 所以可以直接这样 前两个情况的数量相加
    return b
print(f3(4))

# dp问题我们当然也可以按照day99的思路 定义一个 dp数组 具体是几维数组 看变化的维度是几个
def f4(n):
    dp = [0 for _ in range(n+1)]
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[-1]
print(f4(4))
