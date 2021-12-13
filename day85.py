# -- coding: utf-8 --
# Algorithms to Determine a Happy Number
# 检测一个数是否是 happyNumber 啥意思呢？ 
# Input: n = 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1  得到1以后 1的平方=1 不断都是1了 那就是快乐的
# 如果 Input: n = 2 就不是    因为最后是某个无限循环   因为无线循环 且不是都是1 那么 就是 sad不快的

# 我们看一个数是不是sad那么就需要nb来存储已经看过的
def isHappy(n):
    nb = set()
    while n != 1 and n not in nb: #如果是1无线循环了 肯定不会进入while
        nb.add(n)
        cur = n
        # 我们需要求出每一位的平方的和 根据前面的 用//= %就可以
        a = 0
        while cur > 0:
            a += (cur % 10) ** 2
            cur //= 10
        n = a
    return n == 1

print(isHappy(19))
print(isHappy(2))

def isHappy2(n):
    # 我们可以把内部while的部分换成字符串也可以
    nb = set()
    while n != 1 and n not in nb:
        nb.add(n)
        cur = n
        # 我们需要求出每一位的平方的和 根据前面的 用//= %就可以
        a = 0
        for i in str(n):
            a += int(i) ** 2
        n = a
    return n == 1

print(isHappy2(19))
print(isHappy2(2))

def isHappy3(n):
    # python也有更舒服的方式来写str for循环
    nb = set()
    while n != 1 and n not in nb:
        nb.add(n)
        n = sum([int(x)**2 for x in str(n)])
    return n == 1

print(isHappy3(19))
print(isHappy3(2))