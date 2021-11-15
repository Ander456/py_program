# -- coding: utf-8 --
# Algorithms to Search in a Binary Search Tree
# 二叉树搜索树的搜索
# 如day7说的 二叉树就是 子节点最多有两个的树 而 二叉搜索树是左子节点全部小于父节点 右子节点全部大于父节点的二叉树

class BinarySearchTree:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def search(self, root, value):
        if root is None:
            return False
        if root.value == value:
            return True
        if root.value < value:
            return self.search(root.right, value)
        return self.search(root.left, value)

    def search2(self, root, value):
        while root:
            if root.value == value:
                return True
            if root.value < value:
                root = root.right
            else:
                root = root.left
        return False

bst = BinarySearchTree(10)


# bst search的时间复杂度是 o(logn) 当然前提是这个树是平衡的
# 什么是平衡的 就是 最深和最浅的 叶节点的深度相差 <= 1
# 如果是 非常不平衡的树那么 search的复杂度就退化成了o(n)