# -- coding: utf-8 --
# Find the Inorder Successor of a Binary Search Tree
# 在二叉搜索树中查找后继节点的算法
# 后继节点就是最小的比我们要找的节点大的节点 inorder是顺序的

# 我们当然可以inorder排序 然后插入到list里然后 找到目标返回目标下一个
def f(root, t):
    data = [] # list容器插入inorder的节点
    def dfs(root):
        nonlocal data
        if root is None:
            return 
        dfs(root.left)
        data.append(root.val)  # inorder就是放中间
        dfs(root.right)
    dfs(root)
    i = data.index(t)
    if i + 1 < len(data):
        return data[i+1]

# 时间复杂度O(N) 空间O(N)

# 既然是bfs树。。我们当然可以利用特性来 每次遍历消去一半
def f2(root, t):
    ans = None
    while root:
        if t < root.val: #如果目标值t小于当前节点值 那么表明当前节点是一个大于目标的值 
            ans = root.val
            root = root.left # 但是我们还要看看 有没有更小的比目标值小的节点
        else:
            root = root.right  # 如果当前目标值大于 节点值 那肯定还需要往右找
    return ans
# 时间复杂度O(logN) 空间复杂度O(1) 优于第一种方法   (logN 好于 N 但是NlogN 不好于 N)