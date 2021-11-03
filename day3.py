# -- coding: utf-8 --
# Computing Fibonacci Numbers using 3 Methods
# 计算菲波那切数列 也就是求斐波那契数列上的数是几
# 0、1、1、2、3、5、8、13、21 ....
# 求第n个斐波那契数列的数

# 递归方式
def f(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return f(n - 1) + f(n - 2)


print(f(6))


# 迭代方式 取巧了
def f2(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


print(f2(6))


# 递归的方式虽然可以计算出结果但是你在画节点树的时候会发现比如f(5) 会计算两次f(3) 因为f(5) = f(4) + f(3） 而f(4) = f(3) + f(2) 为了避免重复计算我们使用notebook记录
def f3(n, nb={}):
    if n in nb:
        return nb[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    ans = f3(n - 1, nb) + f3(n - 2, nb)
    nb[n] = ans
    return ans


print(f3(6, {}))
