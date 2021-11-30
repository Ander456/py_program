# -- coding: utf-8 --
# Compute the Kth Last Node and Length of a Linked List
# 求单向链表倒数第K个节点(和链表长度算法)

# 我们当然可以 先遍历一遍找到 链表的所有节点个数 然后 sum个数-k得到 第n个节点然后遍历过去找到就行 

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

    def addNode(self, val):
        node = Node(val)
        self.next = node
        return node

def getLength(head):
    ans = 0
    while head:
        ans += 1
        head = head.next
    return ans

def getLength2(head):
    if head is None:
        return 0
    return 1 + getLength2(head.next)
# 我们这里又可以体会一下递归思想的巧妙 
# A->B->C->D    递归我们可以想象成 A -> [B->C->D] 那就是1 + 递归  也就是递归返回的是我们要的 我们要什么？我们要后面的个数 用当前个数1 + 后面即可


# 前面我们快慢指针求middle节点 这里 求倒数第k个 也很简单 
def klast(head, k):
    fast = head
    for i in range(k):
        fast = fast.next
    while fast:
        fast = fast.next
        head = head.next
    return head


head = Node(0)
p = head
for i in range(1, 9):
    p = p.addNode(i)

print(getLength(head))
print(getLength2(head))

print(klast(head, 2).val)