# -- coding: utf-8 --
# Sudoku Validator/Algorithm using 27 Hash Sets
# 用27个哈希集合来验证数独是否有效
# 为什么是27 ？ 因为 行9 列9 然后 每3个组成一个box 一共9个box

# n = 9 where n is number of rows and columns in matrix
# Example 1
# Input
# matrix = [
#     [4, 2, 6, 5, 7, 1, 3, 9, 8],
#     [8, 5, 7, 2, 9, 3, 1, 4, 6],
#     [1, 3, 9, 4, 6, 8, 2, 7, 5],
#     [9, 7, 1, 3, 8, 5, 6, 2, 4],
#     [5, 4, 3, 7, 2, 6, 8, 1, 9],
#     [6, 8, 2, 1, 4, 9, 7, 5, 3],
#     [7, 9, 4, 6, 3, 2, 5, 8, 1],
#     [2, 6, 5, 8, 1, 4, 9, 3, 7],
#     [3, 1, 8, 9, 5, 7, 4, 6, 2]
# ]
# Output
# True

def validSudokuGame(matrix):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [[set() for _ in range(3)] for _ in range(3)]
    for r in range(9):
        for c in range(9):
            x = matrix[r][c]
            if x < 1 or x > 9:
                return False
            if x in rows[r]: #表示当前行有这个数了
                return False
            if x in cols[c]: #表示当前列有这个数了
                return False
            if x in boxes[r//3][c//3]:
                return False # 表示当前九宫格里有这个数了
            rows[r].add(x)
            cols[c].add(x)
            boxes[r//3][c//3].add[x]
    return True

# 时间复杂度O(1) 空间复杂度O(1)  因为一共就81个格子 时间复杂度描述的是 随着N增加而变化的 这里 是固定的