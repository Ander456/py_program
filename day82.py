# -- coding: utf-8 --
# Recursive Algorithm to Merge Two Binary Trees
# 用递归来merge 两个二叉树
# merge两个二叉树的意思是 相同位置的节点上的val 相加  

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def mergeBinaryTree(A, B):
    if A is None:
        return B
    if B is None:
        return A
    C = TreeNode(A.val + B.val)
    C.left = mergeBinaryTree(A.left, B.left)
    C.right = mergeBinaryTree(A.right, B.right)
    return C

# 时间复杂度O(N+M) 空间复杂度O(max(M,N))