# -- coding: utf-8 --
# Compute the Average and Median
# 求平均数和中位数

def average(nums):
    return sum(nums) / len(nums)

def median(nums):
    a = len(nums)
    nums.sort()
    if a % 2 == 0:
        print(nums[a//2])
        print(nums[a//2-1])
        return (nums[a//2] + nums[a//2-1])/2
    else:
        return nums[a//2]


print(average([1,2,3,4,5]))

print(median([1,2,3,4,5]))
print(median([1,2,3,4,5,6]))