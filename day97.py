# -- coding: utf-8 --
# Recursive Algorithm to Find the Sum of Two Numbers in BSTs
# 用递归算法 求解 一个目标和 在两颗 二叉搜索树上各取一个值 是否存在
# 我们知道BST的特性是 左子上的数都比根小右子树上的数都比跟大
# 然后我们各取一个 加起来和 目标值相比 如果 大了 根据bst的特性我们可以任意选一颗数往左 其他同理

def checkSumOfBST(a, b, T):
    if a is None or b is None:
        return False
    if a.val + b.val == T:
        return True
    if a.val + b.val > T:
        return checkSumOfBST(a.left, b, T) or checkSumOfBST(a, b.left, T)
    return checkSumOfBST(a.right, b, T) or checkSumOfBST(a, b.right, T)
# 时间复杂度（最坏的时候O(a*b) 空间复杂度O(1)