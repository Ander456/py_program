# -- coding: utf-8 --
# Two Sum Algorithm when Array is Sorted
# 有序数组的双和算法

# Example 1:
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

# Example 2:
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]

# Example 3:
# Input: numbers = [-1,0], target = -1
# Output: [1,2]

# 注意因为有序 我们才能用双指针 

def twoSum(nums, target):
    def binary_search(n):
        i,j = 0, len(nums)-1
        while i <= j:
            mid = (i+j)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                j = mid-1
            else:
                i = mid+1
        return - 1
    for i in range(len(nums)):
        x = binary_search(target - nums[i])
        if x >= 0 and x != i:
            return [min(i + 1, x + 1), max(i+1, x+1)]

# 时间复杂度O(N*log(N)) for循环N  二分是logN

def twoSum2(nums, target):
    def binary_search(i, j, n):
        while i <= j:
            mid = (i + j)//2
            if nums[mid] == n:
                return mid
            if nums[mid] < n:
                i = mid + 1
            else:
                j = mid -1
        return -1
    for i in range(len(nums)):
        x = binary_search(target - nums[i])
        if x >= 0 and x != i:
            return [min(i + 1, x + 1), max(i+1, x+1)]


def twoSum3(nums, target):
    i, j = 0, len(nums)-1
    while i < j:
        if nums[i] + nums[j] == target:
            return [i+1, j+1]
        elif nums[i] + nums[j] < target:
            i+=1
        else:
            j-=1
