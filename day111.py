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
    def dfs(cur, ans):
        if cur == len(nums): # 数量够了
            ans.append(deepcopy(nums))
            return
        for i in range(cur, len(nums)):  # for 循环从cur到n-1 每一个都尝试下 也就是 cur这个位置每一个数都尝试下的思想
            nums[i], nums[cur] = nums[cur], nums[i] # 交换  
            dfs(cur + 1, ans) # 交换完cur之后 cur+1 然后问题变成了 右边的几个数组 接着再求同一个问题 n-1一个数的全排列
            nums[i], nums[cur] = nums[cur], nums[i]
    ans = []
    dfs(0, ans)
    return ans

# The time complexity is O(N!) and so is the space complexity.
print(f([1,2,3]))

# 其实 每一次递归 我们都是让问题 变成了更小的问题 然后 递归解决 更小的问题 
# 比如上面 的 dfs(cur+1, ans) 目的就是 我们尝试了 第cur个位置后 加入是三个数（那首位 分别 swap了自己 和第二个 和第三个）
# swap了一个后 比如swap了自己 然后 游标cur+1 到了第二个 这个时候 问题变成了 排列后面两个数 所以我们递归 