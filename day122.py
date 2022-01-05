# -- coding: utf-8 --
# Sibling Node in a Binary Search Tree
# 二叉搜索树中寻找兄弟节点

def findSlibing(root, k):
    slibing = -1
    while root:
        if k < root.val:  # 如果我们的k找的值比root小 那么k的兄弟肯定在root右边
            slibing = root.right.val
            root = root.left
        elif k > root.val:
            slibing = root.left.val
            root = root.right
        else:
            return slibing
    return slibing

# 时间复杂度O(logN) 因为用了二分搜索

# 递归方法
def findSlibing2(root, k):
    def dfs(root, slib, k):
        if root.val == k:
            return slib
        if k < root.val:
            return dfs(root.left, root.right.val, k)
        return dfs(root.right, root.left.val, k)
    return dfs(root, -1, k)