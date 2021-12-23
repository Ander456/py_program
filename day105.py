# -- coding: utf-8 --
# Is Subsequence Algorithm via Two Pointer
# 用双指针检测 一个字符串是否是另一个字符串的子串  注意顺序不能更改

def isSubSeqence(s, t):
    ls, lt = len(s), len(t)
    i = j = 0
    while i < ls and j < lt:
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == ls

# 时间复杂度O(N) 空间复杂度O(1)

s = "eric"
t = "eerriicc"
print(isSubSeqence(s, t))
