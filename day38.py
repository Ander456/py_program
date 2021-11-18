# -- coding: utf-8 --
# Prefix Sum Algorithm to Compute the Interval Sums
# 前缀和 算法 来求 区间和 
# 啥意思呢 给定一列数 [1,2,3,4,5] 让你求区间[1,3](索引)的和也就是2+3+4 = 9

class PrefixSum:
    def __init__(self, nums):
        self.nums = nums
        self.computePrefixSum()
    
    def computePrefixSum(self):
        s = 0
        self.prefixSum = [0]
        for i in self.nums:
            s += i
            self.prefixSum.append(s)
        # 上面是典型的空间换时间我们先把所有的前缀和结果计算出来存起来

    def sum(self, frm , to):
        return self.prefixSum[to + 1] - self.prefixSum[frm]

arr = PrefixSum([1,2,3,4,5])
print(arr.sum(1, 3))

# 为啥这么做呢？ 因为如果我们每次都去for循环求 那么时间复杂度是O(N)如果内部嵌套一些query逻辑那么就是O(N*M)
# 这样做之后 负责度变成了O(1) 即使内部嵌套复杂的query逻辑也是O(M)
# 空间换时间

def sum(arr, frm ,to):
    s = 0
    for i in range(frm, to + 1):
        s += arr[i]
    return s

print(sum([1,2,3,4,5], 1, 3))