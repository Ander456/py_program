# 3 Different Approaches to Solve Two-Sum Problem
# 双数之和

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] + nums[j] == target:
                return True
    return False


print(twoSum([1,2,3,4,5], 8))


# 上面的方案有点复杂了 我们可以用一个notebook存下我们目标值然后遍历看是否有目标值
def twoSum2(nums, target):
    nb = {}
    for i in nums:
        if target - i in nb:
            return True
        nb[i] = True
    return False


print(twoSum2([1,2,3,4,5], 10))


# 双指针
def twoSum3(nums, target):
    nums.sort()
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] + nums[right] == target:
            return True
        if nums[left] + nums[right] < target:
            left += 1
        else:
            right -=1
    return False


print(twoSum3([1,2,3,4,5], 9)) 

