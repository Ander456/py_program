# -- coding: utf-8 --
# Three Sum Algorithm
# 三数之和 day9 day123说过了两数之和

def threeSum(nums, target):
    nums.sort() # 排序后才能用多指针法 
    n = len(nums)
    for i in range(n):
        j, k = i+1, n-1
        while j < k:
            if nums[i] + nums[j] + nums[k] == target:
                return True
            elif nums[i] + nums[j] + nums[k] < target:
                j += 1
            else:
                k -=1
    return False
# 时间复杂度O(N平方）