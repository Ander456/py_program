# -- coding: utf-8 --
# Depth First Search to Sum Root to Leaf Numbers in Binary Tree
# 深度优先算法求根节点到叶子数字之和 参考day120

def dfs(root, cur):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return root.val + cur * 10
    a = dfs(root.left, root.val + cur * 10)
    b = dfs(root.right, root.val * cur * 10)
    return a + b

# 时间复杂度O(N) 空间复杂度同（只不过是系统stack帮我们创建的)