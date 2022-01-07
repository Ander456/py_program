# -- coding: utf-8 --
# Maximum Level Sum of a Binary Tree using BFS Algorithm
# 广度优先算法找层节点和最大的那一层
# 每一层的数加起来 计算和

from collections import deque

def maxLevelSum(root):
    if root is None:
        return 0
    q = deque([root])
    maxLvl = maxSum = -float("inf")
    lvl = 1
    while len(q) > 0:
        sz = len(q)
        s = 0
        for _ in range(sz):
            x = q.popleft()
            s += x.val
            if x.left:
                q.append(x.left)
            if x.right:
                q.append(x.right)
        if s > maxSum:
            maxSum = s
            maxLvl = lvl
        lvl += 1
    return maxLvl

# 时间复杂度O(N) 空间同 因为我们需要遍历n个节点并且用deque存储n个节点