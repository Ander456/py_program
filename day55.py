# -- coding: utf-8 --
# Algorithm to Transpose a Matrix
# 求矩阵的逆矩阵

A = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

B = [
    [1,2,3],
    [4,5,6]
]

def pirntMatrix(A):
    for r in A:
        # 每一行
        print(r)

# pirntMatrix(A)
# print("-------------")
# pirntMatrix(B)

def transpose(A):
    R, C = len(A), len(A[0])
    # 逆矩阵的行 == 原来矩阵的列 列==原来矩阵的行
    T = [[None] * R for i in range(C)]
    # 前面的 [None] * R 表示的 R列[None]  得到结果[None, None, None] 如果R是3
    # 后面for i in range(C) 表示 执行C次for循环 C如果是3 那么就是 3行
    # print(T)
    # 也可以这样 创建二维数组 T1 = [[0 for i in range(C)] for j in range(R)]
    #print(T1)
    for r in range(R):
        for c in range(C):
            T[c][r] = A[r][c]
    return T

pirntMatrix(transpose(A))

pirntMatrix(transpose(B))


# 在python里 已经有 现成的方法了
def transpose2(A):
    return list(zip(*A))


pirntMatrix(transpose2(A))