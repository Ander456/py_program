# -- coding: utf-8 --
# Recursive Permutation Algorithm
# 返回一组数的全排列

# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]

# Example 3:
# Input: nums = [1]
# Output: [[1]]

from copy import deepcopy

def f(nums):
    def dfs(left, ans):
        if left == len(nums): # 数量够了
            ans.append(deepcopy(nums))
            return
        for i in range(left, len(nums)):
            nums[i], nums[left] = nums[left], nums[i] # 交换
            dfs(left + 1, ans)
            nums[i], nums[left] = nums[left], nums[i]
    ans = []
    dfs(0, ans)
    return ans

# The time complexity is O(N!) and so is the space complexity.
print(f([1,2,3]))