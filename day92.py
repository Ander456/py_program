# -- coding: utf-8 --
# The Left Side View of Binary Tree via Breadth First Search
# 从左边看一个二叉树 得到的 list

from collections import deque

def leftView(root):
    if root is None:
        return []
    q = deque([root])
    ans = []
    while len(q) > 0:
        sz = len(q)
        for i in range(sz): # 为什么要用sz for 因为 二叉树的某一个level 某一层 可能有N多个 节点 而不止两个 
            p = q.popleft()
            if p.left:
                q.append(p.left)
            if p.right:
                q.append(p.right)
            if i == 0:          # 我们从左边看肯定只取最左边的  如果从右边看那么这里就是i == sz-1
                ans.append(p.val)
    return ans
