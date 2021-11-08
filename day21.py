# -- coding: utf-8 --
# MergeSort Algorithm Simply Explained
# 合并排序

# 思想和快排有点像 同时复杂度 也很像 合并排序时间复杂度是O(n*log(n))稳定的 因为每次pivot我们取的都是middle
# day19学了merge两个有序数列 而mergesort就用到了它 我们将一列数一分为两份 然后 去merge这两部分

# 首先把day19的 merge拿过来
def merge(a,b):
    c = []
    i, j, la, lb = 0 ,0 ,len(a), len(b)
    while i < la and j < lb:
        if a[i] < b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1
    
    while i < la:
        c.append(a[i])
        i+=1
    while j < lb:
        c.append(b[j])
        j+=1
    return c

def mergeSort(n):
    if len(n) <= 1: # 一列数不断的一分为2 直到小于等于1个的时候那肯定是已经排好序的因为一个数啊就
        return n
    mid = len(n) // 2
    left = mergeSort(n[:mid])
    right = mergeSort(n[mid:])
    return merge(left, right)



print(mergeSort([3,1,6,9,2,2,3,5,4]))
