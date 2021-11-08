# -- coding: utf-8 --
# Merge Two Sorted Lists
# 合并两个有序列表

# 其实就是 用两个指针关联两个数列 然后 不断比较 并移动指针

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


print(merge([1,3,4,4,7,9], [2,4,6,8,10]))    # 时间复杂度是 O(len(a)+len(b))

def merge2(a,b):
    c = a + b
    c.sort()
    return c


print(merge([1,3,4,4,7,9], [2,4,6,8,10]))    # 时间复杂度是 O(n * log(n)) 显而易见上面的更好



