# -- coding: utf-8 --
# Binary Search Algorithm to Find First Bad Version
# 用二分搜索 求 第一个 不同的数
# 比如[0,0,0,0,0,0,1,1,1,1,1,1] 求第一个变成1的位置 其实就是

def isBadVersion(i):
    return i == 1

def firstBad(n):
    for i in range(len(n)): #防止是最后一个数
        if isBadVersion(n[i]):
            return i
# 时间复杂度O(N)

a = [0,0,0,0,0,0,1,1,1,1,1,1]
print(firstBad(a))


def firstBad2(n):
    left, right = 0, len(n)
    while left <= right:
        mid = (left + right) /2
        if isBadVersion(n[mid]):
            right = mid - 1
        else:
            left = mid + 1
        return mid

print(firstBad2(a))
