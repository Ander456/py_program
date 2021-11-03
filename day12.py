# -- coding: utf-8 --
# How to Check if Two Strings Anagrams?
# 检测两个字符串是否是 相同字母异序词 比如 listen -- silent 相同字母长度相同但是顺序不同

from collections import Counter, defaultdict


def isAnaGram(s1, s2):
    if len(s1) != len(s2):
        return False
    a,b = {},{}
    for i in s1:
        if i not in a:
            a[i] = 1
        else:
            a[i] += 1
    for i in s2:
        if i not in b:
            b[i] = 1
        else:
            b[i] += 1
    return a == b       # python 可以直接比较 {}dict


print(isAnaGram("tean", "neat"))


# 可以直接用python的counter来返回一个已经计算好的dict
def isAnaGram2(s1, s2):
    d1 = Counter(s1)
    d2 = Counter(s2)
    return d1 == d2

print(isAnaGram("tean", "neatd"))


def isAnaGram3(s1, s2):
    d1 = defaultdict(int)
    d2 = defaultdict(int)
    for i in s1:
        d1[i]+=1
    for i in s2:
        d2[i]+=1
    return d1 == d2


print(isAnaGram("tean", "neat"))
