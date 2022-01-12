# -- coding: utf-8 --
# BFS Algorithm to Check the Completeness of a Binary Tree
# 广度优先算法来判断是否是完整二叉树
# 完全或者完整二叉树 首先是二叉树 然后每一层可能除了最后一层 都被填充了 
# In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
# 满二叉树又是特殊的完全二叉树 最后一层也都被填充满了

# 我们想怎么样判断二叉树是完全二叉树？ 那么就是 下一个node之前不能有空的 

from collections import deque

def f(root):
    if root is None:
        return True
    q = deque([root])
    hole = False # 是否有hole 有空的洞
    while len(q) > 0:
        p = q.popleft()
        if p is None:
            hole = True
        else:
            if hole:
                return False # 如果之前有洞了那肯定不是了
            q.append(p.left)
            q.append(p.right)
    return True
# 时间复杂度O(N) 空间同
