# -- coding: utf-8 --
# Binary and Decimal Conversion Algorithms
# 二进制和十进制转换

# 我们要知道 10进制 也就是 用0-9这个十个数就位基础base的 
# 同理 二进制 就是用0 1这两个数作为base的 

# 十进制的 12345 其实用十进制的表示 是1 * 10的4次方 + 2 * 10的3次方 + 3 *10的2次方 + 4 * 10的1次方 + 5 * 10的0次方
# 同理 二进制 111  是 1*2的2次方 + 1*2的1一次方 + 1 * 2的0次方 

# n is decimal number
def d2b(n):
    ans = ""
    while n > 0:
        ans = str(n % 2)  + ans
        n >>= 1
    return "0" if ans == "" else ans


# n is string
def b2d(n):
    ans = 0
    for i in n:
        ans = ans * 2 + int(i) # 这里*2其实和左移一位一个意思 我们十进制转二进制的时候不断除以2取余 那么往回返肯定是乘以2
    return ans

def b2d2(n):
    ans = 0
    index = len(n)-1
    for i in n:
        ans += int(i) * 2**index
        index -=1
    return ans


print(d2b(5))

# print(b2d("101"))
print(b2d("11011"))
print(b2d2("11011"))