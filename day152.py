# -- coding: utf-8 --
# N-ary Tree Preorder Traversal using Iterations or Recursion
# 先序遍例N叉树的递归和迭代算法

# 递归写法 同二叉树一样写在最前面就行
def preorder(root):
    if root is None:
        return []
    ans = [root.ans]  # 前序遍历 就放着 放最前面
    for x in root.children:  # 如果是二叉树这里直接是 ans += preorder(root.left) ans += preorder(root.right)
        ans += preorder(x)
    return ans


# 非递归  我们要用到stack 其实就是自己用stack来实现计算机帮你递归的stack
def preorder2(root):
    if root is None:
        return []
    stack, output = [root], []
    while stack:
        root = stack.pop() #弹出最后一个
        output.append(root.val)
        stack.extend(root.children[::-1]) #把children reverse下放进stack 方便弹出最左边
    return output

# 时间复杂度都是O(N) 因为我们要处理n个节点