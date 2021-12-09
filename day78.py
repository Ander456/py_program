# -- coding: utf-8 --
# BFS to Check if All Leaves in Same Level of Binary Tree
# 用广度优先bfs 来检测 树的所有叶子节点是否在同一level 同day77 我们依然用一个set来保存左右的最大深度

from collections import deque  # day51介绍过 dequeue

def checkLeavesSameLevel(root):
    if root is None:
        return True
    d = set()
    q = deque([(root, 0)])
    while len(q) > 0:
        cur, depth = q.popleft()
        if cur.left is None and cur.right is None:
            # 那cur就是叶子节点
            d.add(depth)
            if len(d) > 1:
                return False
        if cur.left:
            q.append((cur.left, depth + 1))
        if cur.right:
            q.append((cur.right, depth + 1))
    return len(q) == 1

