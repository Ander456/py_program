# -- coding: utf-8 --
# Palindrome Count Algorithm
# 通过指定字符串构造回文字符串算法
# Example 1
# Input
# s = “ab”
# k = 4
# Output
# 4
# Explanation
# We can make these palindromes [“aaaa”, “bbbb”, “abba”, “baab”].
# k是4表示我们要使用k个数字 那么每个位置的选择也就是 k 那对应的镜像位置也得是k  因为as many as 所以 第二个位置同样也可以是k个选择 这样就只是 奇数和偶数的差异

def f(s, k):
    t = len(set(s))
    if k % 2 == 0:
        return t**(k//2)
    return t**(k//2) * t

#时间复杂度O(N+logN)  因为set操作时间复杂度O(N)  t**(k//2) 是logK的时间复杂度