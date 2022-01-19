# -- coding: utf-8 --
# Set Split Algorithm

# Givena list of positive integers nums, return whether you can divide the list into two groups a and b such that:

# The sum of a and the sum of b are equal.   条件1
# Every number in a is strictly less than every number in b. 条件2 A组里的数都比B组里的小

# Constraints
# 1 ≤ n ≤ 100,000 where n is the length of nums.
# Example 1
# Input
# nums = [4, 9, 5]
# Output
# True
# Explanation
# We can have a = [4, 5] and b = [9] and both of their sums are 9.

# Example 2
# Input
# nums = [9, 9]
# Output
# False
# Explanation
# We can have a = [9] and b = [9] but it doesn’t meet this criteria: “Every number in a is strictly less than every number in b.”


def f(nums):
    nums.sort() # 排序的目的更方便的满足条件2 
    s = sum(nums) # 求出和 因为分两组 和相等 想求出总的来
    if s % 2 == 1:
        return False  # 分不成两组相等的
    # 如果能分成 检测条件2
    c = 0
    for i in range(len(nums) - 1):
        c += nums[i]
        if c * 2 == s and nums[i] < nums[i+1]:
            return True
        if c * 2 > s:
            return False
    return False
# 时间复杂度O(NLogN) sort是这个复杂度

print(f([4,9,5]))
