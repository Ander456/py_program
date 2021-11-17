# -- coding: utf-8 --
# Count the Number of Nodes in Binary Tree using DFS and BFS
# 用dfs和bfs来计算二叉树有多少个节点

# 我们拿到根节点然后 + 左边所有节点数 + 右边所有节点数 = 总数
# 其实到这我们也应该能感觉到了 这种不断深入去查找计数等等的尝试的 都可以用dfs 也就是不断深入尝试
def countWithDfs(root):
    if root is None:
        return 0
    return 1 + countWithDfs(root.left) + countWithDfs(root.right)


# bfs 就是要用队列 没别的说的
def countWithBfs(root):
    if root is None:
        return 0
    q = [root]
    ans = 0
    while len(q) > 0:
        p = q.pop(0)
        ans += 1
        if p.left:
            q.append(p.left)
        if p.right:
            q.append(p.right)
    return ans
