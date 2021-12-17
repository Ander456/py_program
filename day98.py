# -- coding: utf-8 --
# Introduction to Dynamic Programming Algorithm
# 介绍动态规划，终于到了动态规划了 
# day3的时候 用递归 计算了斐波那契额数列 

def f(n):
    if n == 0 or n == 1:
        return n
    return f(n - 1) + f(n - 2)

# 上面的时间复杂度是O(2的n次方) 比如 n=10 然后 我们要计算9和8 binarytree的形式 然后不断分下去 所以是这么个复杂度
# 为啥复杂度这么高 是因为我们重复计算了很多 f(4) 也需要f(3) f(5) 也需要f(3)
# 
#  我们怎么避免重复计算？？ 当然是notebook
# 

def f2(n, nb = {}):
    if n == 0 or n == 1:
        return n
    if n in nb:
        return nb[n]
    val = f(n -1) + f(n-2)
    nb[n] = val
    return val

# 这样我们的时间复杂度就变成了 O(N) 我们计算n=10 那么我们只需要计算出1-10十个数 就行了 

# 上面这种其实是dynamic program的 一种 top-down也就是从上往下的形式  也就是我们解决问题的顺序和方向 这里我们要计算10我们需要9和8 要9就需要7和8 ... 不断的知道找到最小的问题结果1和0 
# 同时也有另一种 从下往上 bottom-top 的形式 如果我们能得到1-10的f(n) 那么我们也就相当于用了nb保存了下来 我们拿到f(0) f(1) 然后求出f(2) 然后不断往上求 直到到目标f(10)

def f3(n):
    f0, f1 = 0, 1  # 最下面的最小结果 
    for i in range(n):
        f0,f1 = f1, f0+f1  # 从小往上 不断求
    return f1

# ynamic Programming aka DP, is a popular technique to optimise the algorithms.
# The main purpose of DP is avoid re-calculating the intermediate results. For example,
#  f you are given 5 apples, and some minutes later, you are given another one, 
# you know you have 5+1 apples in total without needing to re-count the 5 apples. 
# In computer, we can save the known solutions in a cache i.e. memoization.