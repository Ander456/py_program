# -- coding: utf-8 --
# Binary Tree Traversal Algorithms
# 遍历二叉树的方法  

class BinaryTree:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    # 前序遍历 也就是 父-左-右
    def preorder(self, root):
        print(root.value)
        self.preorder(root.left)
        self.preorder(root.right)

    # 中序遍历 左-父-右
    def inorder(self, root):
        self.inorder(root.left)
        print(root.value)
        self.inorder(root.right)

    # 后序遍历 左-右-父
    def postorder(self, root):
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.value)

    # 层序遍历 一层一层遍历 如day7
    def levelorder(self, root):
        if root is None:
            return 
        q = [root]
        while len(q) > 0:
            p = q.pop(0)
            print(p.value)
            if p.left:
                q.append(p.left)
            if p.right:
                q.append(p.right)
        
# 有一个很巧合的事情 就是 如果是 二叉搜索书 BST 那么 BST的 中序遍历 inorder 的结果 就是 in order的 
# 英文里 in order 表示的就是 按顺序  而 inorder 遍历也正巧是这样 太6了day