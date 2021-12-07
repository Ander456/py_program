# -- coding: utf-8 --
# Adding Two Linked Lists
# 相加两个链表 
# 1-2-3 + 4-8-6   5-0-0-1

# 一般我们操作两个链表或者多个链表 最终要得到一个新的的
# 我们都可以 使用一个dummpy 链表作为 结果 参考 day57 66

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

    def addNode(self, val):
        node = Node(val)
        self.next = node
        return node


def addList(a, b):
    dummy = Node(-1)
    head = dummy
    carry = 0
    while a or b or carry:
        cur = carry
        if a:
            cur += a.val
            a = a.next
        if b:
            cur += b.val
            b = b.next
        carry = cur // 10
        cur = cur % 10
        head.next = Node(cur)
        head = head.next
    return dummy.next


n1 = Node(1)
p = n1
p = p.addNode(2)
p = p.addNode(3)

n2 = Node(4)
p = n2
p = p.addNode(8)
p = p.addNode(6)

def printLinkedList(head):
    while head:
        print(head.val)
        head = head.next


printLinkedList(addList(n1, n2))