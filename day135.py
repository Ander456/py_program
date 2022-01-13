# -- coding: utf-8 --
# Depth First Search Algorithms to Determine a Univalue Binary Tree
# 同day117 只不过换成了dfs

def uniqueVal(root):
    if root is None:
        return True
    data = set()
    def dfs(root):
        if root is None:
            return 
        nonlocal data
        data.add(root.val)
        dfs(root.left)
        dfs(root.right)
    dfs(root)
    return len(data) == 1
# 时间复杂度O(N) 空间同 因为我们遍历n个节点 也用到了set

def uniqueVal2(root):
    def dfs(root):
        if root is None:
            return set()
        data = set([root.val])
        data = data.union(dfs(root.left))
        data = data.union(dfs(root.right))
    data = dfs(root)
    return len(data) == 1

def uniqueVal3(root):
    if root is None:
        return True
    def dfs(root, v):
        if root is None:
            return True
        if root.val != v:
            return False
        return dfs(root.left, v) and dfs(root.right, v)
    return dfs(root, root.val)
