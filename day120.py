# -- coding: utf-8 --
# BFS Algorithm to Sum Root to Leaf Numbers in Binary Tree
# 广度优先算法 来 计算 二叉树root到leaf的和

from collections import deque

def f(root):
    if root is None:
        return 0
    q = deque([root, root.val])
    ans = 0
    while len(q) > 0:
        p, x = q.popleft()
        if p.left is None and p.right is None: #叶子节点
            ans += x
        if p.left:
            q.append([p.left, 10 * p.left.val])
        if p.right:
            q.append([p.right, 10 * p.right.val])
    return ans
# 时间复杂度O(N) 空间同  因为要遍历N个节点