# -- coding: utf-8 --
# Revisit the Symmetric Binary Tree by Using Clone and Invert
# 判断一个二叉树是否是 对称的  用clone和 invert

# copy 有两种 deep copy and shadow copy
# shadow 就是个别名 拥有了一堆别名而已 其实本身还是原来的引用 
# deep 就是完全的一个新的

class Tree:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def cloneBinaryTree(root):
    if root is None:
        return None
    newRoot = Tree(root.val)
    newRoot.left = cloneBinaryTree(root.left)
    newRoot.right = cloneBinaryTree(root.right)
    return newRoot

# 时间复杂度O(N) 因为我们需要遍历n个节点

def equalTree(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    return a.val == b.val and equalTree(a.left, b.left) and equalTree(a.right, b.right)
# 时间复杂度O(min(n,m))
# 这里还是典型的递归思想 递归返回的即是我们想要的 不要自己脑袋里去穷举 很累很笨

# day62的invert
def invert(root):
    if root is None:
        return None
    left = invert(root.left)
    right = invert(root.right)
    root.left = right # 这里其实又是递归的思想我们不纠结自己脑海穷举 而是说我们要的是已经翻转好的节点 root.left = invert(root.right)
    root.right = left
    return root

def isBinaryTreeSymeetric(root):
    copyTree = cloneBinaryTree(root)
    copyTree = invert(copyTree)
    return equalTree(root, copyTree)
# 这个太耗理解了。。你克隆了一个树 然后 invert镜像翻转它 如果这俩数还想等 那肯定这个树就是 symmetric的 镜像树啊

