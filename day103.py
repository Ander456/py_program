# -- coding: utf-8 --
# Dynamic Programming Algorithm to Count Bits for N Integers
# 用动态规划求 给定一个数n 求1-n 之间的所有数二进制表示的时候 包含多少个 二进制的1

# day75 和day74 都讲了 一个数是否是2的幂3的幂 其实本质是 二进制里的 1的shift 和n&(n-1) 来消1法

# 笨办法我们当然可以for循环 依次求出每一个数的二进制1的个数然后相加

def count1(x):
    ans = 0
    while x > 0:
        x &= (x-1)
        ans += 1
    return ans

def f(n):
    ans = [0]
    for i in range(1, n+1):
        ans.append(count1(i))
    return ans
# 时间复杂度O(N*logN)
print(f(2))

# 我们可以看出来 比如 12的二进制1100 8的二进制1000  我们知道8里面有1个1 12里面有几个1不需要再重头计算了 只需要有8的结果然后+1就可以了
def f2(n):
    ans = [0]
    for i in range(1, n+1):
        ans.append(ans[i & (i-1)] + 1)  # 也可以是 ans.append(ans[i>>1] + i&1) #不断消shift然后+是否是1的数
    return ans
print(f2(2))
# 时间复杂度变成了O(N) 这是dp形式的 top-bottom 方式 我们要求 ans[i] 那么我们需要求出 ans[i % (i-1)] 也就是消了一个1的数的结果 然后 + 1 不断求最小的  只不过这里我们直接有了记忆 不需要重复计算 