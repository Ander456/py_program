# -- coding: utf-8 --
# Reverse a Graph (Adjacency List)
# 翻转一个图  图的定义参考day44
# Given a directed graph represented as an adjacency list, 
# return its reverse so if an edge goes from A to B, it now goes from B to A.

# example  graph = [[2,3],[1],[2]] 表示 顶点1指向2和3 2指向1 3指向2

def reverseGraph(graph):
    rev = [[] for _ in range(len(graph))] # 创建一份原来图的复制(只包含顶点不包含指向）
    for u, v in enumerate(graph): # u是顶点 v是从这个u指向的顶点的列表
        for k in v: # 我们迭代原来顶点指向的顶点然后 翻转
            rev[k].append(u)
    return rev

# 时间复杂度O(VE) V定点数E边数
