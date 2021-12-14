# -- coding: utf-8 --
# Using Hash Set or Hash Table to Count Next Element
# 计算 下一个数出现的次数 比如[1,2,2,3,5,7]   1下一个数2出现的次数2  2下一个数3出现次数1 总共3  其他的没有下一个数了


def CountNextElement(nums):
    nb = set(nums)
    ans = 0
    for i in nums:
        if i + 1 in nb:
            # 下一个数在nb里
            ans += 1
    return ans
# 时间复杂度O(N)
print(CountNextElement([1,2,2,3,5,7]))

# 我们当然也可以无脑两层for
def CountNextElement2(nums):
    ans = 0
    for i in nums:
        for j in nums:
            if j == i + 1:
                ans += 1
                break
    return ans

def CountNextElement3(nums):
    ans = 0
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] + 1 == nums[i]:
                ans += 1
                break
    return ans
print(CountNextElement3([1,2,2,3,5,7]))
# 时间复杂度O(N方)

from collections import Counter

def CountNextElement4(nums):
    d = Counter(nums)
    return sum(v for k, v in d.items() if k + 1 in d)

print(CountNextElement4([1,2,2,3,5,7]))