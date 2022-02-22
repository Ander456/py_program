# -- coding: utf-8 --
# Algorithms to Compute the Range Sum of a Binary Search Tree
# 二叉搜索树区间求和的算法
# 给定区间[low, high] 求所有在这个区间里的节点的和

from inspect import stack


def rangeSumBST(root, low, high):
    if not root:
        return 0 
    ans = 0
    if root.val >= low and root.val <= high:
        ans += root.val
    ans += rangeSumBST(root.left, low, high)
    ans += rangeSumBST(root.right, low, high)
    return ans

# 优化下 因为如果root不在区间其实没必要让 left right再递归了
def rangeSumBST2(root, low, high):
    if not root:
        return 0 
    ans = 0
    if root.val >= low and root.val <= high:
        ans += root.val
    if root.val > low:
        ans += rangeSumBST2(root.left, low, high)
    if root.val < high:
        ans += rangeSumBST2(root.right, low, high)
    return ans

# 改写成非递归的 那就是我们自己用stack模拟系统stack
def rangeSumBST3(root, L, R):
    if not root:
        return 0
    ans = 0
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            if L <= node.val <= R:
                ans += node.val
            if L < node.val:
                stack.append(node.left)
            if node.val < R:
                stack.append(node.right)
    return ans


# 时间复杂度O(H) H是树的高度 因为我们用了二分 H=log(N)