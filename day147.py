# -- coding: utf-8 --
# Unobstructed Buildings via Monotonous Decreasing Stack
# 通过隔楼看海问题 引出 单调递减栈 

# Example 1
# Input
# heights = [1, 5, 5, 2, 3]
# Output
# [2, 4]
# Explanation
# We can see the ocean in building heights[2] and heights[4].

# Example 2
# Input
# heights = [5, 4, 3, 2, 1]
# Output
# [0, 1, 2, 3, 4]
# Explanation
# We can see the ocean in every building since each building is taller than every other on its right.

# Example 3
# Input
# heights = [1, 1, 1, 1, 1]
# Output
# [4]
# Explanation
# We can’t see the ocean in any building other than the last one.

# input的数据每一幢楼的高度 海在右边 我们要求出能看到海的楼的索引 

# 方法1 brute 也就是直接的粗暴的遍历

def f(nums):
    if not nums:
        return []
    n = len(nums)
    ans = []
    for i in len(n):
        anyTall = False
        for j in len(i+1, n): # 我们遍历所有的看看右边有没有高于或者等于 这个楼的楼 如果没有那么久可以看到
            if nums[j] >= nums[i]:
                anyTall = True
                break
        if not anyTall:
            ans.append(i)
    return ans
# 时间复杂度O(N平方) 空间O(N)但是因为我没有不去遍历空间ans 其实也可以理解为O(1)空间直接输出了

# 方法2 我们可以提前计算出 每一个楼 右边最高的楼有多高
import math
def f2(nums):
    maxRightHeight = -math.inf
    ans = []
    n = len(nums)
    for i in range(n-1, -1, -1): # 从右向左遍历
        if nums[i] > maxRightHeight: # 如果当前的高于从右到现在最高的那么它肯定能看到海
            ans.append(i)
        maxRightHeight = max(maxRightHeight, nums[i])
    return ans[::-1]
# 时间复杂度O(N) 空间O(1)

# 方法3 我们用单调递减栈来解决 
# 单调 首先要满足 然后是 递减 也就是 要维持这个栈 一直是从大到小的 
def f3(nums):
    stack = []
    for i, v in enumerate(nums):
        while stack and nums[stack[-1]] <= v: # 这表示栈顶的数小于当前的v 那么我们就要把栈顶的小于的全部弹出去
            stack.pop()
        stack.append(i)
    return stack
# 时间复杂度O(N) 空间O(N)
