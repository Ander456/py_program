# -- coding: utf-8 --
# Find the Single Number in Array
# 找到数组中 单个的数 [1,1,2,2,3,4,4] 3就是单个的数 

# 如果不是单个的那么他们互相与上肯定结果是0 那么单个数最后与上的就是它自己了
def singleNum(nums):
    ans = 0
    for i in nums:
        ans = ans ^ i
    return ans

from collections import Counter

def singleNum2(nums):
    d = Counter(nums)
    for i in d.keys():
        if d[i] == 1:
            return i

print(singleNum([1,1,2,2,3,4,4]))

print(singleNum2([1,1,2,2,3,4,4]))

# def singleNums3(nums):
#     return reduce(lambda a, b: a^b, nums, 0)