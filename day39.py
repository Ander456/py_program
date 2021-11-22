# -- coding: utf-8 --
# The Linked List Data Structure
# 链表 
# 链表 和 数组是两个最基本的数据结构
# 数据内存连续  查找O(1) 增删O(N)  链表增删O(1) 查找O(N)
# 数组地方不够了要扩容 你就想象成你一个衣服柜子满了 要找一个更大的柜子把所有衣服都搬过去

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def addNode(self, value):
        node = Node(value)
        self.next = node
        return node


head = Node(0)
p = head
p = p.addNode(-1)
for i in range(10):
    p = p.addNode(i)

p = head
while p:
    print(p.value)
    p = p.next      