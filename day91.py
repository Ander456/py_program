# -- coding: utf-8 --
# Recursive Depth First Search to Compare Leaf Equivalent Trees
# 用递归和深度优先 来比较 两棵二叉树的 叶子节点是否相同 

def sameLeaves(a, b):
    def dfs(root):
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [root.val]
        return dfs(root.left) + dfs(root.right)
    return dfs(a) == dfs(b)

# 时间复杂度O(N+M) 空间同