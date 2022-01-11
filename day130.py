# -- coding: utf-8 --
# Depth First Search to Find the Only Child in Binary Tree
# 深度度优先算法找单孩子节点 也就是这个节点是父节点唯一的孩子节点那么它就是 only child

def dfs(root, cnt): # root和当前root孩子数
    if root is None:
        return 0
    ans = 0
    if cnt == 1:
        ans += 1
    x = 0
    if root.left:
        x += 1
    if root.right:
        x += 1
    ans += dfs(root.left, x)
    ans += dfs(root.right, x)
    return ans

# 时间复杂度O(N) 
# 还是标准递归思想 我们要求二叉树的什么 那就是分别求 左和右的 然后 左右的又是递归问题
# 比如我们这里求 总共的 单孩子节点数 那么分别求出左右单孩子节点数就行

