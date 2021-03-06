# -- coding: utf-8 --
# Dynamic Programming to Compute the Derangement Permutations
# 用动态规划求 乱序组合的 数量 
# deragement 是 ragment的反义词 ragement表示按顺序排列也就是1在1的位置2在2的位置 
# 乱序就是每一个数都不在自己原来的位置上

# 我们brute 暴力想法 如何检测一个数是否是乱序？遍历一次 那时间复杂度是O(N) 
# 然后所有的组合数呢？ O(N!) 那暴力法的 时间复杂度O(N!*N) 很可怕

# 动态规划  TOP DOWN DYNAMIC PROGRAMMING 
# 我们可以这么想 n个数 我们第n个数肯定不能在n的位置上 才行 
# 那么可以有 n-1个位置可以选 ， 那如果选了k位置 那k位置上原来的数 就有两种情况
# 1. 直接换到位置n上 那么剩下的就是n-2可以选的位置    2. 不换到n的位置上 那么可以有 （n-1)个位置选择
# (n-1) * f(n-2) + (n-1) * f(n-1)
# 那么状态转移方程是 f(n) = (n-1)*(f(n-1)+f(n-2))
# 这么说 还是不好理解 本质上我们函数f求的是给n个数的乱序组合数量 我们能否找到n-1个数的乱序组合数和这个的关系
# 也就是用记忆memory 用更小的子问题 来帮助我们解决问题
# 我们n个数第n个数肯定只有n-1种选择 那就剩下了（n-1）个数然后我们再求它的乱序组合数 思路就是这样top-down 我们要找到
# 怎么从n-1 能推导到 n

# 上面难点想的是 n个数 你可以理解成3个数来考虑
# 1,2,3    我们把3 选择 只能选择 2个位置 如果被占位置的数不考虑3这个位置 那么其实就是剩下两个数的 递归
# 如果考虑 3这个存在 和它交换 那就是剩下 1个数的递归··

# @cache   # 加了cache就等于用了notebook 只不过计算机帮我们保存了 否则重复计算的时间复杂度是O(2的n次方）
def f(n):
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1
    return (n-1)*(f(n-1)+f(n-2))


# 然后我们还有 bottom-up的 形式
def f2(n):
    # 先定义base case
    dp = [0] * (n+1)
    dp[2] = 1
    # 状态转移方程
    for i in range(3, n+1):
        dp[i] = (i-1) * (dp[i-1] + dp[i-2])  # 这个和斐波那契一样 也可以简化成 a,b = 0, 1 for循环里 a,b = b, (i-1)*(a+b)
    return dp[-1]
# 时间复杂度O(N) 用dp数组空间复杂度O(N)