# -- coding: utf-8 --
# Introduction to Queue Data Structure and Examples
# 队列数据结构 first in first out

# 给一列数 [1,2,3,4]
# 求出这一列数的平方 [1,4,9,16]

def sqr(nums):
    ans = []
    while len(nums) > 0:
        x = nums.pop(0) #默认弹出最后但是如果传入参数弹出参数位置
        ans.append(x*x)
    return ans

print(sqr([1,2,3,4]))