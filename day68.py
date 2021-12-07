# -- coding: utf-8 --
# Algorithm to Check If Array is Monotonic
# 检测一个数组是否是单调的
# 单调包括单调递增 和 单调递减

def isMonotonic(nums):
    increase = True
    decrese = True
    for i in range(len(nums) - 1):
        if nums[i] > nums[i+1]:
            increase = False
        elif nums[i] < nums[i+1]:
            decrese = False
    return increase or decrese

# 时间复杂度 O(N)

print(isMonotonic([1,2,3,4,5]))
print(isMonotonic([15,4,3,2,1]))
print(isMonotonic([1,3,2,5,1]))