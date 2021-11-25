# -- coding: utf-8 --
# Binary Search Algorithm to Compute the Square Root
# 用二分搜索法 计算一个数的开根号的值是多少 比如 4开根号就是2

# 求x的开根号是多少 其实和day46的求log2(x) 思路一样
def sqrt(x):
    if x < 0:
        return None
    if x < 1:
        left, right = 0, 1
    else:
        left, right = 1, x
    # 上面先定了一个大概范围 然后我们要开始用二分法猜了 每次猜的大于或者小于我们就可以舍弃一部分
    cur, mid = 0,0
    while abs(cur - x) > 1e-5: #精度范围
        mid = (left + right)/2
        cur = mid * mid
        if cur < x:
            left = mid
        else:
            right = mid
    return mid


print(sqrt(4))

print(sqrt(16))