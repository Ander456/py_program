# -- coding: utf-8 --
# Backtracking Algorithm to Solve N-queen Problem
# 回溯算法解决 N-皇后问题

# Given NxN chess board, you are asked to place N queens 
# so that they are not attacking each other horizontally, vertically and diagonally. 
# If the requirment is only not being attacked by other queens vertically and horizontally 
# but it is ok to have other queens in four diagonal directions, 
# we can compute the number of placement solution is N! (factorial).

# 如果nxn的棋盘上放n个皇后 保证 在水平 数值 斜方向 都没有其他皇后 这样就okay
# 简单点的n皇后问题 可以是 能够放在斜线上 皇后只会 横竖攻击 那么 这个就很简单 摆法就是n的阶乘
# 你想啊如果可以放斜线 不能同行同列 我们第一个放在 第一列上有n个选择 然后第二个放在第二列上只要不同行那么就是n-1个选择 那么依次就是n！

# 但是如果 斜线不能放呢？ 我们其实还是这个思路 每一列 放一个皇后 
# 第一列第一行先放一个 然后第二列 可以选择的 然后 巴拉巴拉
# The strategy is to try placing current queen, 也就是我们取尝试看看这个位置能不能放
# 也就是在这列选择 每一行 尝试 


# cur当前每一列摆放情况 x要检查是否能放下的行
def can_place(cur, x):
    for i, y in enumerate(cur): # 这个i是索引表示这是哪一列 y是value表示放在了哪一行
        if y == x or len(cur) - i == abs(x - y): #len(cur)当前放了几列了 
            # len(cur) - i == abs(x - y) 这句的目的是 看 横向距离(列差值)和纵向距离(行差值)是否相等相等那么构成正方形肯定在对角线上
            return False
    return True 

# cur表示当前的方案也就是当前每一列上的摆放结果
def dfs(cur, n):
    if len(cur) == n: #如果合理的放下了那么表示这是一种结果
        return 1
    ans = 0
    for row in range(n):
        #每一行都尝试下
        if can_place(cur, row):
            #那么我们就放下这个皇后
            ans += dfs(cur + [row], n)
    return ans

# n表示n维nxn的棋盘
def queue(n):
    return dfs([], n)


print(queue(8))
