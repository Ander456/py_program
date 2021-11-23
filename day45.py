# -- coding: utf-8 --
# Palindrome Permutation Algorithm
# 给定一个字符串是否能排列一下这个字符串的字母来形成一个回文串
# 回文串 比如 racecar

# 我们很明显的知道 回文串 如果字母出现次数为1一次(奇数)那么只能允许出现这一个 奇数字母数量大于1那肯定不是回文串
# 如果都是偶数的字母 那肯定可以排列出回文串


from collections import Counter, defaultdict

def check(s):
    d = Counter(s)
    oddCount = 0
    for i in d.keys(): # keys是 所有的key d[i] 返回这个key字母对应的数量
        if d[i] & 1 == 1:
            # 与上1得到奇数肯定是奇数
            oddCount += 1
            if oddCount > 1:
                return False
    return True


print(check("racecar"))
print(check("racecare"))
print(check("racecaree"))
print(check("racecareef"))

# 我们当然也可以不用python内置的Counter函数
def check2(s):
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i]  =1
    oddCount = 0
    for i in d.keys():
        if d[i] & 1 == 1:
            oddCount += 1
            if oddCount > 1:
                return False
    return True

print(check2("racecar"))
print(check2("racecare"))
print(check2("racecaree"))
print(check2("racecareef"))