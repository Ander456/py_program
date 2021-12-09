# -- coding: utf-8 --
# Depth First Search to Check If Leaves Same Level in Binary Tree
# 用深度优先来检测 树的所有叶子节点都在同一level
# 叶子节点就是 没有孩子的节点

# 我们用set保存dfs找到的左右最深的层次 然后 最后 看 set的数量是否为1 如果是 那么表示 所有叶子节点确实统一层要不然肯定 不是 
def checkLeavesSameLevel(root):
    d = set()
    def dfs(root, cur):
        if root is None:
            return 
        if root.left is None and root.right is None:
            d.add(cur) # 叶子节点 因为没有子节点 那么我们记录下当前的level深度
            return
        dfs(root.left, cur + 1)
        dfs(root.right, cur + 1)
    dfs(root, 0)
    return len(d) == 1

# 时间复杂度O(N) 空间复杂度O(N)
        