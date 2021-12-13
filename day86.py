# -- coding: utf-8 --
# Recursive Algorithm to Compute the Maximum Depth of Binary Tree
# 用递归 求一颗二叉树的最大深度 

def maxDepth(root):
    if root is None:
        return 0
    leftDepth = maxDepth(root.left)
    rightDepth = maxDepth(root.right)
    return max(leftDepth, rightDepth) + 1

# 时间复杂度O(N)
# 还是那句老话 递归 别自己脑补 
# 当前递归返回的就是我们要的 我么要什么？左树最大深度 和 右树最大深度 