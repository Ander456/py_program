# -- coding: utf-8 --
# Double-Ended Queue to Perform a BFS to Sum Nodes in a Tree
# 用双端队列 利用BFS 求一个树的所有节点的和
# 主要介绍和使用双端队列

from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
 
    def addLeftChild(self, val):
        newNode = Node(val)
        self.left = newNode
        return newNode
 
    def addRightChild(self, val):
        newNode = Node(val)
        self.right = newNode
        return newNode

def bfsSum(root):
    if root is None:
        return 0 
    ans = 0
    dq = deque()
    dq.append(root)
    while len(dq) > 0:
        p = dq.popleft() # 如果是用list pop（0）时间复杂度是O(N) 而这里是O(1)
        ans += p.val
        if p.left:
            dq.append(p.left)
        if p.right:
            dq.append(p.right)
    return ans

root = Node(1)
root.addLeftChild(2)
right = root.addRightChild(3)
right.addLeftChild(4)
right.addRightChild(5)

print(bfsSum(root))