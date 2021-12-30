# -- coding: utf-8 --
# Find the Lowest Common Ancestor of a Binary Search Tree
# 递归算法求二叉树两节点的共同最低祖先
# 如果 两个节点其中一个是另一个的父节点那么共同最低祖先是 这个父节点 （规定）

# 我们分析 如果给定一个 根节点root 和要找的 p 和 q两节点
# 1. root就是p或者q其中之一
# 2. p q 在root两边 那 root 就是 LCA
# 3. p q 在root的 左边 或者右边 

def f(root, p, q):
    if root is None:
        return None
    if root.val == p or root.val == q:
        return root
    left = f(root.left, p, q) # 找左边 
    right = f(root.right, p, q) # 找右边
    if left is None:
        return right
    if right is None:
        return left
    # 如果 left 和 right都 不为空那就是 在separate
    return root

# 时间复杂度O(N) 因为需要遍历n个节点
