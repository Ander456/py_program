# -- coding: utf-8 --
# Breadth First Search to Find the Only Child in Binary Tree
# 广度优先算法找单孩子节点 也就是这个节点是父节点唯一的孩子节点那么它就是 only child

from collections import deque

def f(root):
    if root is None:
        return 0
    q = deque([root, -1]) # [节点，父节点孩子节点数量]
    ans = 0
    while len(q) > 0:
        cur, cnt = q.popleft()
        if cnt == 1:
            ans += 1
        x = 0
        if cur.left:
            x += 1
        if cur.right:
            x += 1
        if cur.left:
            q.append([cur.left, x])
        if cur.right:
            q.append(cur.right, x)
    return ans

# 时间复杂度O(N) 因为我们遍历所有节点 空间同因为我们用了queue