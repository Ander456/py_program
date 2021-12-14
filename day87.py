# -- coding: utf-8 --
# BFS Algorithm to Compute the Maximum Depth of the Binary Tree
# 结合day86 今天是用BFS 来计算二叉树的最大深度 硕大 BFS就是队列

from collections import deque

def maxDepth(root):
    if root is None:
        return 0
    q = deque([(root, 1)])
    ans = 0
    while len(1) > 0:
        cur, depth = q.popleft()
        ans = max(ans, depth)
        if cur.left:
            q.append((cur.left, depth + 1))
        if cur.right:
            q.append((cur.right, depth + 1))
    return ans

# 时间复杂度O(N) 空间复杂度O(N)