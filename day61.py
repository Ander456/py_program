# -- coding: utf-8 --
# Search in a 2D Sorted Matrix
# 在2D 有序矩阵中 搜索值
M = [
    [1,4,7],
    [2,5,8],
    [3,6,9]
]

# M就是一个sorted matrix 因为 每一行 都是从小到大 每一列依然是从小到大 

# M矩阵 T要搜索的值
def search1(M, T):
    for r in M:
        for c in r:
            if c == T:
                return True
    return False

print(search1(M, 5))
# 时间复杂度O(M * N) M行N列

# 既然是排序好的那么就是单调的 既然是单调的曲线 那么我们肯定可以有二分或者 其他方式来优化
def search2(M, T):
    Rows = len(M)
    if Rows == 0:
        return False
    Cols = len(M[0])
    if Cols == 0:
        return False
    R, C = 0, Cols - 1
    # 我们选定 矩阵右上角为起点
    while R < Rows and C >= 0:
        if M[R][C] == T:
            return True
        elif M[R][C] > T:
            # 如果大于T那么我们需要往左走
            C -= 1
        else:
            # 如果小于 那么我们需要往下走
            R += 1
    return False

print(search2(M, 8))
print(search2(M, 0))