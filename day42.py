# -- coding: utf-8 --
# Introduction to Heap and Priority Queue
# 二叉堆 结构 和 优先级队列

# 堆 通常都是二叉树 而且是 完全二叉树  因为堆基本用来做优先级队列 利用二叉树的性质 来加速 查找 和 找最大 找最小的速度
# 二叉树: 最多有两个子节点的树
# 完全二叉树： 一棵深度为k的有n个结点的二叉树，对树中的结点按从上至下、从左到右的顺序进行编号，
#           如果编号为i（1≤i≤n）的结点与满二叉树中编号为i的结点在二叉树中的位置相同，则这棵二叉树称为完全二叉树。
#           其实就是从上到下从左到右排布
# 满二叉树： 就是子节点满的 完全二叉树


import heapq as hq

data = [3,2,1]
hq.heapify(data) #O(N) build a heap

# while len(data) > 0:
#     print(hq.heappop(data))

hq.heappush(data, 5)
hq.heappush(data, -1)

# while len(data) > 0:
#     print(hq.heappop(data))

print(hq.nlargest(2, data))
print(hq.nsmallest(2, data))

print(hq.heappushpop(data, 10))
# while len(data) > 0:
#     print(hq.heappop(data))

print(hq.heapreplace(data, -3))
print(hq.heappop(data))




