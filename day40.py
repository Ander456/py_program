# -- coding: utf-8 --
# Fast and Slow Pointer to Obtain the Middle of the Linked List
# 快慢指针找链表中间的值

# 我们当然可以先遍历一遍链表拿到count然后再遍历一次到中间 但是这样太蠢了

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def addNode(self, value):
        node = Node(value)
        self.next = node
        return node

def mid(head):
    fast, slow = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow

head = Node(0)
p = head
for i in range(1, 10):
    p.addNode(i)
    p = p.next

print(mid(head).value)