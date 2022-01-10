# -- coding: utf-8 --
# Algorithms to Find Center of Star Graph
# 找 星星图 中心
# 星星图就是 一个center中心 然后 其他node都链接这个中心的 图 
# 我们在day44中介绍过图 就是点和边组成的

# 我们从星星图的定义就能看出来 center的 入度（也就是进去的边的数量）== n-1

from typing import DefaultDict

def findCenter(edges):
    G = DefaultDict(int)
    for u, v in edges:
        G[u] += 1
        G[v] += 1 # 因为星星图是 无向图 所以 入度 两个节点都要加
    return max(G.items, key=lambda i:i[1])[0] # 返回入度最大的那个节点

# O(N)

# 我们又知道 星星图 那么 肯定是 入度不为1的那个 其他节点入度都为1
def findCenter2(edges):
    G = DefaultDict(int)
    for u, v in edges:
        G[u] += 1
        G[v] += 1
        if G[v] > 1:
            return G[v]
        if G[u] > 1:
            return G[u]
# O(1)

# 同理我们通过方式2也能看出 连续两个节点 入股其中 有一个节点出现在 连续两个边的表示 
# 比如a-b  b-c  那么 b肯定是center

def findCenter3(edges):
    if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
        return edges[0][0]
    return edges[0][1]
# O(1) 
       