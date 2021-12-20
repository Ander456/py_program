# -- coding: utf-8 --
# Count Number of Ways to Walk in a Grid by Dynamic Programming
# 从网格左上角到右下角  只能 向右|向下 移动 一共有多少种方法 
# day93 讲了 排列组合  day98讲了动态规划 
# -------
# |X| | |
# -------
# | | | |
# -------
# | | |T|
# -------

# you have to walk n-1 steps south and m-1 steps east. Therefore, there are n+m-2 steps, and you can pick n-1 or m-1 for south or east. That is C（n+m-2, n-1) or C(n+m-2, m-1) (这两数一样因为从5个苹果里拿3个和拿2个。。结果是一样的组合)
def countWays(n, m):
    def C(N, M):
        if M == N or M == 0:
            return 1
        if M == 1:
            return N
        return C(N - 1, M - 1) + C(N - 1, M) 
    return C(n+m-2, n-1)

print(countWays(2,2))

# 当然了我们也可以用动态规划来，比如我们在T目标点 那么我们有几种方法可以走到这呢？肯定是从T的上方或者T的左方
# 那依次类推 。我们有几种方法到T的上方呢？ 一样
def countWays2(n, m, nb = {}):
    if n == 0 or m == 0:
        return 1 # 因为如果第一行或第一列的时候我们要到这只能横着一种或者竖着一种走
    if (n,m) in nb:
        return nb[(n, m)]
    val = countWays(n-1, m) + countWays(n, m-1) # 从上面到的加上从左边到的
    nb[(n,m)] = val
    return val

print(countWays2(2,2))

# 上面这种 是dp问题的 一种 从上到下 up-bottom的 还有一种是 bottom-up的方式
# 也就是我们先知道了左方或者上方的然后不断往右下走
def countWays3(n, m):
    dp = [[0 for _ in range(m)] for _ in range(n)] # 生成二维数组的方法 m是列数 n是行数
    dp[0][0] = 1
    for r in range(n):
        dp[r][0] = 1
    for c in range(m):
        dp[0][c] = 1
    for r in range(1, n):
        for c in range(1, m):
            dp[r][c] = dp[r-1][c] + dp[r][c-1]
    return dp[-1][-1]

print(countWays3(2,2))
# 时间复杂度O(N*M) 因为我们需要走完所有的格子

# 还有一个延伸问题 我们从左上到右下这么走 但是要求中途必须经过某个点P 那这次从左上S到右下T一共多少种方法呢？
# 首先我们可以求出S-P 然后再乘上 P-T就是结果了
