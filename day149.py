# -- coding: utf-8 --
# Subtree with Maximum Value via Recursive DFS Algorithm
# 求子树最大的和 
# 子树 有多少个节点就有多少个子树。。因为 单节点你也能叫它子树 root也是子树 


import math

def maxMumSubTree(root):
   
    ans = -math.inf
    def dfs(root):
        nonlocal ans
        if root is None:
            return 0
        x = root.val + dfs(root.left) + dfs(root.right) # 以root为根节点的这颗子树的所有节点的和
        ans = max(x, ans)
        return x
    return dfs(root)
