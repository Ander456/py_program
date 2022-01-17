# -- coding: utf-8 --
# Finding the Largest Lucky Number in the Array
# 找到数组中最大的lucky number
# [1,2,2,3,4,5] 1-1次 2-2次 3-1次 4-1次 5-1次 lucky number是 number和出现次数一样的数
# 这里有 1 2  我们找最大的 那么就是 2

n = [1,2,2,3,4,5]

from collections import Counter

def findLargestLuckyNumber(nums):
    d = Counter(nums)
    ans = []
    for i in d:
        if i == d[i]:
            ans.append(i)
    if ans:
        return max(ans)
    return -1
# 时间复杂度O(n) 空间O(N)
print(findLargestLuckyNumber(n))

def findLargetsLuckyNumber2(nums):
    ans = -1
    for i in nums:
        x = nums.count(i)
        if x > ans and x == i:
            ans = i
    return ans
# 时间复杂度O(N平方) nums.count是O(N) 空间O(1)
print(findLargetsLuckyNumber2(n))

def findLargestLuckyNumber3(nums):
    nums.sort(reverse=True)
    c = 0
    for i in range(len(nums)):
        c += 1
        if i == len(nums)-1 or nums[i] != nums[i+1]: # 最后一个数或者不一样的时候
            if nums[i] == c: #lucky number c就是counter计数器 来计数一样的数的数量
                return c
            c = 0
    return -1
# 时间复杂度O(nlogN) sort就是这个时间复杂度 O(nlogN) 比for的O(N)大 我们取大的
print(findLargestLuckyNumber3(n))
