# -- coding: utf-8 --
# Find Root of N-Ary Tree using Hash Set
# 找到n叉树的根节点 给定一列节点

def findRoot(tree):
    seen = set()
    for node in tree:
        for child in node.children:
            seen.add(child)
    for node in tree:
        if node.val not in seen:
            return node

# 我们挨个把节点的child都放进set 最后谁没被放进去谁就是root 因为root不是任何人的子