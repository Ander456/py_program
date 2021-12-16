# -- coding: utf-8 --
# Compute the Max Product of 3 Numbers in the Array
# 计算数组中 最大的乘积 by 3个数

def maxProductOf3(nums):
    nums.sort()
    return max(nums[-1]*nums[-2]*nums[-3], nums[0]*nums[1]*nums[-1])

print(maxProductOf3([-200,-100,-1,1,2,3,5]))
print(maxProductOf3([-200,-100,-5,-3,-1]))

# 我们可以看出来如果都是正数那么肯定 排序后最后面几个乘积最大
# 如果都是负数 同理 三个负数乘积 肯定结果还是负数 那么肯定找 还是后面三个乘积的出来的负数最大
# 如果有正有负 那么 俩负数相乘 然后取一个正数这样最大