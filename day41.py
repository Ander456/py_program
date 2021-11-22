# -- coding: utf-8 --
# Algorithms to Find the Cycle of a Linked List
# 检测一个链表是否有环 这个环可以是首尾相连形成的 也可以是 中间任意两个节点相连形成的 只要有环就行

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def addNode(self, value):
        node = Node(value)
        self.next = node
        return node


# 直观上我们当然可以记录下来所有走过的点然后看看下面一个是否已经走过 走过那就有环
def checkCircle1(head):
    nb = set() #空间复杂度O(N)
    while head:
        if head in nb:
            return True
        nb.add(head)
        head = head.next
    return False


# 当然了我们也可以用快慢指针的方法 只要快指针能追上慢指针那么一定有环
def checkCircle2(head):
    fast, slow = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return fast


head = Node(0)
p = head
p = p.addNode(1)
p = p.addNode(2)
p = p.addNode(3)
p.next = head

print(checkCircle1(head))

print(checkCircle2(head))
        
        