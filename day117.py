# -- coding: utf-8 --
# Breadth First Search to Determine a Univalue Binary Tree
# 广度优先 来确定 一颗二叉树 的节点是否 都是 唯一值  也就是 所有节点值都相同
from collections import deque
def f(root):
    if root is None:
        return True
    q = deque([root])
    nb = set() # 记事本用来记录是否唯一
    while len(q) > 0:
        p = q.popleft()
        nb.add(p)
        if p.left:
            q.append(p.left)
        if p.right:
            q.append(p.right)
    return len(nb) == 1

# 时间复杂度O(N) The space complexity is O(N) as we are using a queue to implement the BFS, and the set will only be counted as O(1) as we will exit as long as there is more than 1 distinct numbers in the set.