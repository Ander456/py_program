# -- coding: utf-8 --
# Sorting a Linked List using Merge Sort (Divide and Conquer)
# 用merge sort 排序一个 链表

# merge sort的核心就是找到mid 然后分成两段 不断的递归 最后 merge

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

    def addNode(self, val):
        node = Node(val)
        self.next = node
        return node

def mid(head):
    if head is None or head.next is None:
        return head
    fast, slow = head, head
    prev = None
    while fast and fast.next:
        fast = fast.next.next
        prev = slow
        slow = slow.next
    prev.next = None #这一步是为了断开链表 形成俩链表
    return slow

def merge(a, b):
    # 合并俩链表说白了就是俩指针指着链表然后不断找到当前要的最小值 移动
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

import random

head = Node(100)
p = head
for i in range(10):
    p = p.addNode(random.randrange(10, 2000))

def printNode(head, msg = ""):
    print(msg)
    while head:
        print(head.val)
        head = head.next

printNode(head)

def sortLinkedList(node):
    if node is None or node.next is None:
        return node
    a = sortLinkedList(mid(node))
    b = sortLinkedList(node)
    return merge(a,b)

printNode(sortLinkedList(head))