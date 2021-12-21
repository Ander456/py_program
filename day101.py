# -- coding: utf-8 --
# Dynamic Programming to Obtain Max Non-Neighbour Values
# 动态规划解决打家劫舍问题  
# 也就是 给定一列数表示 一排房子所拥有的钱 我们的贼 要偷里面的钱 但是前提是 不能偷连着的房子（可能会被警察抓走） 求 贼能偷到的最多钱

# 我们可以这么分析，贼偷到最后一座房子的钱的可能结果是 max(H(n) + f(n-2), H(n-1)) 也就是 两种情况么 偷这个最后的房子 （从n-2）偷过来 或者 不偷这房子（前面偷了n-1）
# 那么我们就能 使用dp问题的up-bottom 不断从n找到最小结果1 类似斐波那契数列
v = []
def f(n, nb = {}):
    global v
    if n == 0:
        return v[0]
    if n == 1:
        return max(v[0], v[1])
    if n in nb:
        return nb[n]
    val = max(v[n] + f(n-2), f(n-1)) 
    nb[n] = val
    return val

v = [10,1,5,3]
print(f(len(v)-1))
# 上面这种情况是 dp的 up-bottom形式 我们利用notebook来存储优化计算

# 那同时我们也可以选另一种方式 bottom-up的形式 
# 我们分析出这钱的结果只和 选的房子数量有关系 那么维度就是一维
def f2(v):
    n = len(v)
    dp = [0] * n # 我们定义一维的数组dp 来表示第i个房子的时候目前偷到的最大的钱数
    if n == 0:
        dp[0] = 0
    if n == 1:
        dp[1] = v[1]
    if n == 2:
        dp[2] =  max(v[0], v[1])
    for i in range(n):
        dp[i] = max(v[i] + dp[i-2], dp[i-1])  # 这个其实就是 状态转移方程了
    return dp[-1]

print(f2(v))
# Algorithms are in O(N) time and O(N) space. 