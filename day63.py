# -- coding: utf-8 --
# Recursive Algorithm to Determine if a Binary Tree is Symmetric
# 用递归来确定一个树 是否是 对称树 也就是 左右两边是镜像翻转的

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

root = Node(1)
left = root.addLeftChild(2)
right = root.addRightChild(2)
right.addLeftChild(4)
right.addRightChild(5)

def symmetric(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    return a.val == b.val and symmetric(a.left, b.right) and symmetric(a.right, b.left)
    # 这里又是递归思想如果 你自己脑海里去穷举想 会很容易短片 短路 
    # 我们就在这一步就只考虑 递归返回的结果 是我们想要的就行了 比如 symmetric(a.left, b.right) 这就是我们要的结果
    # 这就是电影院前排人返回来的第一排我们要知道的信息 你管他中间经历了多少排呢 脑补肯定晕 
    # 你就要这个结果就行了  就一句  递归返回的是我们想要的结果 不要脑补

print(symmetric(root.left, root.right))

left.addLeftChild(5)
left.addRightChild(4)

print(symmetric(root.left, root.right))