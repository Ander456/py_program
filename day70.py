# # -- coding: utf-8 --
# Pythagorean Triplets in Array using Two Pointer or Hash Set
# 勾股定理三角形直角三角形   判断一个数组里的数 是否有满足直角三角形的 用双指针或者notebook set
# [3,1,4,7,5] 这里 3 4 5 就可以满足
# 直观的 我们可以 for循环三次 逐个遍历来检测

l = [3,1,4,7,5]

# 这里多补充下 这种for循环形式 range是从0开始到n-1不包含n 
# 内层循环for x in range(外层当前值) 这样就很巧妙的实现每次取三个不同的值 然后做一个操作
# 而不是 每次都for i in range(n)  这样就会取到相同的值 
# 而如果我们一般思维 是什么呢？ 先取一个i然后里面的从i+1开始 然后再内层再+1 这样写+1不是不行 就是有点不美
# 我们每次都用range 外层for循环 来达到 一个 内外不相同 但是都可以遍历的效果 就很优雅
def Pythagorean(nums):
    n = len(nums)
    for i in range(n):  
        for j in range(i):
            for k in range(j):
                if nums[i]**2 == nums[j]**2 + nums[k]**2:
                    return True
    return False
# 时间复杂度 O(N的三次方)
print(Pythagorean(l))

# 我们用notebook 存储来优化下
def Pythagorean2(nums):
    nb = set()
    n = len(nums)
    for i in range(n):
        nb.add(nums[i]**2)
    for i in range(n):
        for j in range(i):
            if nums[i]**2 + nums[j]**2 in nb:
                return True
    return False
# 时间复杂度 O(N) + O(N平方) 那么最终是O(N平方) 空间复杂度O(N)
print(Pythagorean2(l))

# 双指针 这种 。。知道两个然后对三个关系就可以确定的。。就可以用双指针 套路就是先排序 然后 两个指针移动来求值
def Pythagorean3(nums):
    n = len(nums)
    nums.sort(reverse=True) #从大到小排序 这一步 时间复杂度O(N*logN)
    for i in range(n):
        l = i + 1 # 第二个数
        r = n - 1 # 最后一个数
        while l < r:
            if nums[l]**2 + nums[r]**2 == nums[i]**2:
                return True
            elif nums[l]**2 + nums[r]**2 > nums[i]**2:
                # 如果大了那说明 我们改取一个更小的
                l += 1
            else:
                r -= 1
    return False
# 时间复杂度 O(N*logN) 和 O(N平方)[for循环嵌套while就是N方] 最终取O(N方） 空间复杂度 O(1)
print(Pythagorean3(l))