# -- coding: utf-8 --
# Using Binary Search to Find K-th Largest Number in Array
# 用二分搜索法 找到 数组中 第k大的数 

# 我们当然可以直接排序 然后找索引
def findKLargest(nums, k):
    nums.sort()
    return nums[-k] #倒数第k个

a = [1,4,6,8,3,9,8]

print(findKLargest(a, 3))
# 但是上面这时间复杂度是 O(N)

def findKLargets2(nums, k):
    def countHowManyLargerOrEqualThan(n):
        ans = 0
        for i in nums:
            if i >= n:
                ans += 1
        return ans
    left, right = min(nums), max(nums)
    while left <= right:
        mid = (left + right) // 2
        x = countHowManyLargerOrEqualThan(mid)
        if x >= k:
            left = mid + 1 #表明我们找的小了那么改下left counter找到的是 大于等于这个数的数量 
        else:
            right = mid - 1
    return right

print(findKLargets2(a, 3))

# 时间复杂度 O(Nlog(N))