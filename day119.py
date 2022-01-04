# -- coding: utf-8 --
# Two Sum Algorithm
# 双数之和 哈哈哈 面试最简单的

def f(nums, T):
    for i in range(nums):
        for j in range(i):
            if nums[i] + nums[j] == T:
                return [i, j]

# 时间复杂度O(N平方)

def f2(nums, T):
    seen = {}
    for i,v in enumerate(nums):
        if T-i in seen:
            return [i, seen[T-i]]
        seen[v] = i
# 时间复杂度O(N) 空间同