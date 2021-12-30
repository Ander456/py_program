# -- coding: utf-8 --
# Dynamic Programming to Compute the Triangle Minimum Path Sum
# 动态规划计算三角形 最短路径
# Example 1:
# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# For each step, you may move to an adjacent number of the row below.
# 比如 如上图三角形 我们从2开始走 怎么走到最下面 和 最小 最小和是 11 2-3-5-1
# 2
# 3 4
# 6 5 7
# 4 1 8 3
# 转换成这样的形式 更方便写成二维数组 

# 状态转移方程是
# 我们定义f(r,c) 是 当前到r,c的 最小值 那 f(r,c) 和 r+-1 c+-1的关系是什么呢？
# 我们每次只能选 左或者右 那么当前是最小的 那上面的从那走过来的肯定是两个选择中的较小值
# 即 f(r,c) = min(f(r+1, c), f(r+1, c+1)) + f(r,c)

# top-down形式
def minPathSum(T):
    #@cache
    def f(r,c):
        if r == len(T) - 1: # 最后一行
            return T[r][c]
        return min(f(r+1,c), f(r+1,c+1)) + T[r][c]
    return f(0,0) # 为啥最后是0，0？因为我们算法本质是从最下面开始计算的  从0到最下层 最小 和最下层到0，0最小是一样的
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(minPathSum(triangle))
# 如果不加cache 时间复杂度 O(2的n次方)   加了 O(r*c)

# bottom-up形式
def minPathSum2(T):
    for r in range(len(T) - 2, -1 ,- 1): #从倒数第二行开始
        for c in range(len(T[r])): # 这一行的列遍历
            T[r][c] = min(T[r+1][c], T[r+1][c+1]) + T[r][c]
    return T[0][0]
print(minPathSum2(triangle))
# 时间复杂度O(r*c)
