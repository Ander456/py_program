# -- coding: utf-8 --
# Reverse a Linked List using Recursion and Iterative Algorithms
# 逆转一个链表 用递归 和 迭代两种方法

# A->B->C->D    变成  A<-B<-C<-D

# 递归方案 
def revere(head):
    if head is None or head.next is None:
        return head # 比如上面走到D就返回了 这个时候D就是head
    n = revere(head.next)
    # 这里多说几句 这就是递归的思想 我们不要去自己深入想 我们就想 递归返回的是我们这里的下一个 
    # 就想电影院从后往前问第一个人的名字 这里返回的肯定是当前我们前面人给我们的结果 
    # 而这里我们要处理的是什么 逆转链表 那这里返回的是什么？肯定是 前面已经逆转好的链表（递归return的就是我们要的） 也就是 当前的head点的下一个点啊 
    # 那我们要干嘛呢？ 只需要把我们当前自己head和别人返回告诉我们的点 逆一下 即可 其他的工作计算机递归都帮我们做了 
    # 递归不要自己去穷举试那样很容易晕 我们就清楚的记得 我们要的结果是什么 递归返回的肯定是当前情况的下一个人告诉我们的要的结果
    head.next.next = head  # A的next是B 这里我们bucare后面的递归什么结果我们这里就是要让B.next 变成A
    head.next = None
    return n

# 还有一个很有意思 我们肯定可以用两个指针来不断搬动链表给他每一个都反过来
# 想想一下 链表是一条铁轨 我们找俩人 每一节都逆转下 
def reverse2(head):
    prev = None
    cur = head
    # 上面是我们找的俩人
    while cur:
        temp = cur.next
        # 逆转
        cur.next = prev
        prev = cur # 下面这两行其实就是让这俩指针移动到下一节
        cur = temp
    return prev
