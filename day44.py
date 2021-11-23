# -- coding: utf-8 --
# Introduction to Graph Data Structure
# 图 数据结构
# 从day1到目前 的数据结构有 list stack queue tree(binary tree) linked-list  heap
# 树结构可以看做是图  链表结构也可以看做是图
# 图是什么 G(V,E) 有顶点和 边的 就是图 
# 当然了 有边 那么边上就会有 权重 和 方向  所以也就有了 有权图 和无权图   有向图 和 无向图
# For number of incoming edges, we call it the incoming degree, 
# and for number of outgoing edges for a vertex, 
# we call it the outgoing degree.
# 也即是说 对于 进入这个顶点的边 我们称作 进度  出去的称作 出度  用度来表示边的多少

# 我们存储图 或者表示图 怎么来表示呢？
# 1. 链接矩阵  2. 邻接表

G = [
    [0,1,0] # edges from vertex 0 也即是从0顶点出发能去的顶点
    [1,0,1] # edges from vertex 1
    [0,1,0] # edges from vertex 2
]
# (0) <--> (1) <--> (2) 上面的 邻接矩阵 用来 存储 这个 图
# 邻接矩阵的好处是 我们 可以直接找到 给定一个点是否能去目标点 但是 缺点是 nxn的空间 很多时候是浪费的

G2 = {
    "A" : ["B"],   # key是起点 value是能去的顶点
    "B" : ["A", "C"],
    "C" : "B"
}
# (A) <--> (B) <--> (C) 上面的邻接表 表示法 能够存储 我们这行这个图


# We can also store the weights by using the tuples: 如果有权重的话我们可以通过 tuple来存储
G = {
    "A" : [("B", 1)],
    "B" : [("A", 2), [("C", 3)]],
    "C" : [("B", 4)]
}
# 当然了 我们可以用字典来存储带权重的图
G = {
    "A" : {"B" : 1}, # 注意字典是 key 冒号: value
    "B" : {"A" : 2, "C" : 3},
    "C" : {"B" :4}
}

