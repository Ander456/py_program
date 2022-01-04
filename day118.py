# -- coding: utf-8 --
# Recursive Backtracking Algorithm to Compute the Combinations
# 递归组合算法 day111 讲的是返回全排列 这里求的是 所有的组合结果

# Example 1:
# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
# 其实就是 给4个苹果 从里面拿2个有几种组合形式

def combine(n, k):
    ans = []
    def dfs(left, cur):
        if len(cur) == k:
            ans.append(cur[:]) #这个就和deepcopy一个效果
        for i in range(left, n+1):
            cur.append(i)       # 选择第i个
            dfs(i + 1, cur)     # 选择下一个
            cur.pop()           # reset
    dfs(1, [])
    return ans

print(combine(4, 2))
# 时间复杂度O(C(n,k)) 空间同