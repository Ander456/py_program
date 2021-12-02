# -- coding: utf-8 --
# Invert a Binary Tree in 5 Minutes (Google Interview Question)
# 翻转一个 二叉树  其实就是镜像一个二叉树 左边跑右边右边跑左边 这样

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

    # 层序遍历 一层一层遍历 如day7
    def levelorder(self, root):
        if root is None:
            return 
        q = [root]
        while len(q) > 0:
            p = q.pop(0)
            print(p.val)
            if p.left:
                q.append(p.left)
            if p.right:
                q.append(p.right)

def invert(root):
    if root is None:
        return None
    left = invert(root.left)
    right = invert(root.right)
    root.left = right # 这里其实又是递归的思想我们不纠结自己脑海穷举 而是说我们要的是已经翻转好的节点 root.left = invert(root.right)
    root.right = left
    return root

# 时间复杂度是 O(N) 因为要遍历全部节点

root = Node(1)
root.addLeftChild(2)
right = root.addRightChild(3)
right.addLeftChild(4)
right.addRightChild(5)

root.levelorder(root)

invert(root)

root.levelorder(root)




