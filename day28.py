# -- coding: utf-8 --
# Recursive Algorithm to Validate a Binary Search Tree
# 检测二叉搜索树是否合法
# 是否是二叉搜索树也就是满足 首先是二叉树 然后 满足 所有左都小于父节 所有右都大于父节点 即可

# 用一个滑动窗口 min ----- max 来表示我们当前二叉树的最大最小的值 

def checkBST(root, min = -float("inf"), max = float("inf")):
    if root is None:
        return True
    if root.value > max or root.value < min: # 超了窗口限制就说明是不合法的bst
        return False
    return checkBST(root.left, min, root.value) and checkBST(root.right, root.value, max)
    

# 时间复杂度是 O(n) 因为我们所有的n个节点都要去检测