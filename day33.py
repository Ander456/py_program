# -- coding: utf-8 --
# Sum of First N Even Numbers (with Mathematic Induction)
# 前n个偶数的和 

# day32说了前n个奇数的和 然后我们知道前n个数的和是 n(n+1)/2 那么减一下就行了
# 因为前n个偶数的和那么 前n个数的和里的n要换成2n 因为 前2个偶数和+前2个奇数和 一共四个数 才是前x个数的和


def sumOfEven(n):
    return n*n+n

def sumOfEven2(n):
    ans = 0
    for i in range(2, 2*n + 1, 2):  # range的第二个参数是不包括的 [）
        ans+=i
    return ans

print(sumOfEven(3))

print(sumOfEven2(3))