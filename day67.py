# -- coding: utf-8 --
# Algorithms to Compute the Intersection of Two Linked Lists
# 计算两个有序链表的交集
# 1-2-3-4-5
# 6-7-8-然后指向3-4-5
# 那么交集就是 3-4-5

# 简单一点 既然 是有序的 如果有交集 那么肯定是 第一个相同的数出现的时候就是交集开始了
# 我们当然可以用notebook存起来然后看看 第二个里面 有没有 

def getIntersectionNode(A, B):
    d = set()
    while A:
        d.add(A)
        A = A.next
    while B:
        if B in d:
            return B
        B = B.next
    return None


# 当然了  我们可以看出 1-2 长度2  然后 3-4-5 长度 3  6-7-8长度 3  
# 如果我们让A走到头然后再从B开始走 同理B走到头再从A开始走 那么 最终肯定会走到 3这个相同点 因为 2 + 3 + 3  和 3 + 3 + 2 两种走法走了一样的长度
def getIntersectionNode2(A,B):
    a, b = A, B
    while a != b:
        a = a.next if a else B
        b = b.next if b else A
    return a

    