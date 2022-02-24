# -- coding: utf-8 --
# Depth First Search to Convert to Elephant Binary Tree
# 深度优先算法转换成大象二叉树
# 其实就是 root.val 是 root.val + 左右子树valsum

def converToElephantTree(root):
    def dfs(root):
        if not root:
            return 0
        val = root.val
        val += dfs(root.left)
        val += dfs(root.right)
        root.val = val
        return val
    dfs(root)
    return root

# 时间复杂度O(N) 空间同