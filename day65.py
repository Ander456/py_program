# # -- coding: utf-8 --
# Convert a Sorted List to a Balanced Binary Search Tree
# 把有序的列表 转化成一个 平衡二叉搜索树 
# 二叉搜索树 是 左都小于根 右都大于根的二叉树
# 平衡 就是 左右高度差不大于1 

# 我们知道一点是 二叉树的 inorder 遍历 输出结果 正好是 inorder的从小到大的 list
# 那么我们 重建一个 balanceBST 很简单 从中间拿一个数当做 root 然后递归就可以了

class Tree:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def buildBST(nums):
    if nums is None or len(nums) == 0:
        return None
    mid = len(nums) // 2
    root = Tree(nums[mid])
    root.left = buildBST(nums[:mid])
    root.right = buildBST(nums[mid+1:])
    # 这里就是典型的 递归思想了 我们安排好了root 那么 左边的就当做build的nums同理右边的也是 
    # 一般我们自己人脑递归 就是 21行 进去 然后再碰到21行 不断 这样 就会 迷茫 忘记 right
    # 但是我们按照递归的思想 递归返回的是我们要的 那么 我们21行22行就是 这一次递归 一起干的事合成一起看 而不是 自己脑补深入
    return root
