# -- coding: utf-8 --
# Binary Search to Compute the Logarithm Base Two Function
# 用二分搜索 计算一个数以2为底的对数
# log曲线是一条 在y轴右侧 从负数到整数的 单调递增曲线 

def log2(x):
    if x <= 0:
        return None # 2的任何次方都不可能小于0
    if x < 1:
        # 这部分就是 曲线 负数的部分
        return -log2(1/x) #  log(x) = log(1/(1/x)) = log(1/x的-1次方) = -1 * log(1/x) 
    # 剩下的部分 就可以简单的二分查找了 
    left, right = 0, x # 开始从0 - x 猜值
    mid = (left + right) / 2
    cur = 2 ** mid
    while abs(cur - x) >= 1e-8:  #计算机中用e来表示10的几次幂 1e-8表示 10的-8次方 也即是0.00000001 这里就是我们要的这个数的精度其实
        mid = (left + right) * 0.5
        cur = 2 ** mid
        if cur >= x:
            right = mid
        else:
            left = mid
    return mid


print(log2(100))
print(log2(8))