# -- coding: utf-8 --
# Escape Maze by Breadth First Search Algorithm
# 广度优先算法找迷宫出路

# 迷宫如下 1 代表墙  左上入口 右下出口
# matrix = [
#     [0, 1, 0],
#     [0, 0, 1],
#     [0, 0, 0]
# ]

from collections import deque

# BFS
def escapeMaze(matrix):
    if not matrix:
        return -1
    rows = len(matrix)
    cols = len(matrix[0])
    if matrix[0][0] == 1 or matrix[-1][-1] == 1:
        return -1 # 入口出口不能进入
    q = deque([0,0,1])  # [行，列，distance]
    vis = set()
    while q:
        r, c, s = q.popleft()
        if r == rows - 1 and c == cols - 1: # 走到终点了
            return s 
        if (r, c) in vis:
            continue
        vis.add((r, c))
        for dr, dc in [(1,0), (0,1), (-1,0), (0,-1)]: # 4个方向
            nr  = r + dr
            nc = c + dc
            if 0 <= nr < rows and 0 <= cols and matrix[nr][nc] != 1:
                q.append((nr, nc, s+1))
        return -1

# 时间复杂度O(RC) 空间O(RC)
