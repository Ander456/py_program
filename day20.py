# -- coding: utf-8 --
# QuickSort Algorithm Simply Explained
# 快速排序

# 核心思想就是 把一列数分成三部分 小于的 等于的 大于的 （怎么分？随便找一个pivot然后 遍历一次就找到了 这三部分）
# 然后每一个部分 递归 最后 每一个部分 [x] + [y] + [..] 合并起来

import random

def quickSort(n):
    if len(n) <= 1:
        return n
    pivot = random.choice(n)
    smaller = []
    equaller = []
    bigger = []
    for i in n:
        if i < pivot:
            smaller.append(i)
        elif i == pivot:
            equaller.append(i)
        else:
            bigger.append(i)
    return quickSort(smaller) + equaller + quickSort(bigger)


print(quickSort([2,4,6,1,5,7,3]))

# 算法复杂度 最差的时候是O(n平方) 平均是O(n*log(n)) 
# 因为如果pivot取的不好每一次都是 最小或者最大 那么 本来要分三部分 但是相当于没有分开 所以 取了n次 然后每次遍历 那么就是n*n 也即是n的平方
# 但是如果每次pivot取的都很好 都给分成了 三部分 并且smaller bigger里数都很多 那么久相等于 二分了 也就是log(n) 然后乘以n次pivot取操作


def bubbleSort(n):
    length = len(n)
    for i in range(length - 1):   # 表示我们要走 length-1次 也就是冒这么多次泡泡
        for j in range(length - 1 - i): # 表示每次冒泡完一个我们要把冒泡这个排除掉 如果i==0那么表示 length-1这个也就是最后一个数经过这次冒牌下次可以排除掉了
            if n[j] > n[j + 1]:
                n[j], n[j+1] = n[j+1], n[j]
    

arr = [2,4,1,3,5,9,0]
bubbleSort(arr)
print(arr)