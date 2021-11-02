# Introduction to Trees, Binary Trees, Perfect Binary Trees, and BFS.
# 树这种数据结构 是 只有一个根节点 并且所有其他子节点最多只有一个父节点 叶子节点没有kid节点
# binary tree 是一个节点最多只有两个kid节点的树
# perfect binary tree 又是每一个节点都有两个孩子节点 并且所有叶子节点的深度相同
# binary search tree 又是 所有左节点都小于父节点 所有右节点都大于父节点

def bfs(root):
    q = []
    q.append(root)
    while len(q) > 0:
        p = q.pop(0)
        print(p.val)
        if p.left != None:
            q.append(p.left)
        if p.right != None:
            q.append(p.right)
            
