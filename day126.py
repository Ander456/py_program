# -- coding: utf-8 --
# Maximum Level Sum of a Binary Tree using DFS Algorithm
# 深度优先算法找层节点和最大的那一层
# 同day125 只不过 把bfs 换成了 dfs
# 我们思考 求每一层 bfs 简单的角度是因为 bfs天生 按层级 一层一层 进行 
# 我们如果改用dfs 那么我们就需要记住 某一层的 sum 

from typing import DefaultDict


def maxLevelSum(root):
    def dfs(root, level, nb):
        if root is None:
            return
        nb[level] += root.val #计算这一层的sum 累加每次到这一层
        dfs(root.left, level+1, nb)
        dfs(root.right, level+1, nb)
    nb = DefaultDict(int)
    dfs(root, 0, nb)
    return max(nb.items, key=lambda x: x[1])[0]

# 时间复杂度O(N) 空间同 