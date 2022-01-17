# -- coding: utf-8 --
# Construct Binary Tree From Pre/Inorder Traversals
# 根据 前序遍历和中序遍历 重构二叉树
# 二叉树遍历
# 前序  preorder  NLR   (dfs)
# 中序  inorder   LNR
# 后续  postorder LRN
# N node在那个位置就叫什么序

class Tree:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def f(preorder, inorder):
    if preorder is None or inorder is None:
        return None
    rootVal = preorder.pop(0) # preorder的第一个值肯定是 rootNode
    i = inorder.index(rootVal) # 根据rootval 在inorder中找到它 那么左边和右边都是分别是左子树和右子树
    root = Tree(rootVal)
    root.left = f(preorder, inorder[:i])
    root.right = f(preorder, inorder[i:])
    return root
#时间复杂度O(N平方)  pop(0) O(N) index O（N)