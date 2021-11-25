# -- coding: utf-8 --
# Algorithms to Remove Nodes from a Linked List
# 从单链表中移除一个值

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

    def addNode(self, val):
        node = Node(val)
        self.next = node
        return node

def printNode(head, msg = ""):
    print(msg)
    while head:
        print(head.val)
        head = head.next

head = Node(1)
p = head
for i in range(2, 10):
    p = p.addNode(i)

# printNode(head, "before")

def removeNode(head, val):
    if head is None:
        return None
    if head.val == val:
        return head.next
    # 这里又可以看出递归的思想我们不深入 递归返回的就是我们想要的 我们想要什么？当前值的下一个节点 上面一行已经给出来了 
    # 所以我们直接让当前的head的下一个指向我们要的
    head.next = removeNode(head.next, val)
    return head

# removeNode(head, 5)
# printNode(head, "after")

def removeNode2(head, val):
    if head is None:
        return None
    if head.val == val:
        return head.next
    prev = head
    cur = head.next
    while cur:
        if cur.val == val:
            prev.next = cur.next
            break
        prev, cur = cur, cur.next
    return head

# head = removeNode2(head, 1)
# printNode(head, "after")


# 但是我们注意上面的 两种 remove 递归和非递归的 都只能删除一个节点 如果有重复的节点就无法删除
# 比如
p.addNode(5)
printNode(head)

# head = removeNode2(head, 5)
# printNode(head)

# 如何可以删除多个相同的呢？ 我们稍微改造下上面的两个
def removeNode3(head, val):
    if head is None:
        return None
    if head.val == val:
        # 这里原来是返回我们要链接的下一个节点 这里我们可以继续递归 让它继续删除
        return removeNode3(head.next, val)
    head.next = removeNode3(head.next, val)
    return head

# removeNode3(head, 5)
# printNode(head)

def removeNode4(head, val):
    if head is None:
        return None
    if head.val == val:
        return head.next
    prev = head
    cur = head.next
    while cur:
        if cur.val == val:
            prev.next = cur.next
            # 原来这里我们break了 
        prev, cur = cur, cur.next
    return head

head = removeNode4(head, 5)
printNode(head)