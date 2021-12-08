# -- coding: utf-8 --
# Recursive Algorithm to Cut/Trim a Binary Search Tree
# 用递归算法 根据 给定 最小最大值的范围 裁剪一颗 二叉搜索树
# 比如 你二叉搜索树中 包含[1-10] 这10个数 
# 给定范围 [3,7] 那么 最终 小于3 大于7的节点都会被裁减掉 

def cutBST(root, L, R):
    if root is None:
        return None
    if root.val < L:
        # 如果当前值小于最小范围 那么 左子树都可以裁减掉
        return cutBST(root.right, L, R)
    elif root.val > R:
        return cutBST(root.left, L, R)
    # 如果当前值在范围内 那么我们就要去处理它的左右子树
    root.left = cutBST(root.left, L, R)
    root.right = cutBST(root.right, L, R)
    return root

# 时间复杂度O(N) 因为我们需要遍历全部树节点