# # -- coding: utf-8 --
# Divide and Conquer Algorithm to Merge K Sorted Linked List
# merge k个 排序好的linked list
# day57 是如何merge两个sorited linked list
# 那么如何mergek个？？ 简单啊。。我们可用第一个merge第二个然后 merge第三个。。

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

    def addNode(self, val):
        node = Node(val)
        self.next = node
        return node

def merge(a, b):
    dummpy = Node(-1)
    p = dummpy
    while a and b:
        if a.val < b.val:
            p.next = a
            a = a.next
        else:
            p.next = b
            b = b.next
        p = p.next
    if a:
        p.next = a
    if b:
        p.next = b
    return dummpy.next

def mergeKSortedLinkedList(lists):
    if len(lists) == 0:
        return None
    ans = lists[0]
    for i in range(1, len(lists)):
        ans = merge(ans, lists[i])
    return ans
# 时间复杂度 是O(K*N) merge操作复杂度是O(N)


# 我们当然也可以利用merge的思想 先把lists 一分为二 不断的一分二为2 分解成小问题小情况 然后 再merge 起来 
def mergeKSortedLinkedList2(lists):
    l = len(lists)
    if l == 0:
        return None
    if l == 1:
        return lists[0]
    if l == 2:
        return merge(lists[0], lists[1])
    mid = l // 2
    # left = lists[:mid] 我第一次写的时候 直接写成了这样。。太傻逼了 不写递归 直接 left = 一块数组 。。。
    # right = lists[mid+1:]   
    # 下面还是递归的思想 我们要的left和right就是递归返回给我们的
    left = mergeKSortedLinkedList2(lists[:mid])
    right = mergeKSortedLinkedList2(lists[mid+1:])
    return merge(left, right)
# 时间复杂度还是O(K*M)  O(logN)出现在我们一分为二后另一部可以抛弃的情况
# 这里我们即使/2了但是 另一部分节点我们还是需要遍历 。。所以 