# -- coding: utf-8 --
# Two Array Intersection Algorithms
# 求两个数组的 交集  也就是 这些数字A有 B也有的

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]

# notebook
from collections import Counter

def f(A, B):
    n1 = Counter(A)
    n2 = Counter(B)
    ans = []
    for i in n1:
        if i in n2: # 如果这个数字在n2中也存在 那就是 交集部分啊
            for _ in range(min(n1[i], n2[i])):
                ans.append(i)
    return ans

nums1 = [1,2,2,1]
nums2 = [2,2]
print(f(nums1, nums2))
# 时间复杂度 O(N+M) 空间复杂度同

# 一般这种 两个 集合的 都能用双指针法 
def f2(A, B):
    A.sort()
    B.sort()
    ans = []
    i = j = 0 # 双指针
    la , lb = len(A), len(B)
    while i < la and j < lb:
        if A[i] == B[j]:
            ans.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    return ans

print(f2(nums1, nums2))
# 时间复杂度 O(NlogN) 因为sort的时间复杂度是这个 下面while的 不够大 舍弃了