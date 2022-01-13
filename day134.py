# -- coding: utf-8 --
# Reverse Bits of a 32-bit Integer
# 翻转二进制的32位 

def reverseBinary(n):
    ans = 0
    p = 31 # 一共有31位需要处理
    while n > 0:
        ans |= (n & 1) << p  # n&1是为了看最右边是1还是0 然后 右移31位是为了放到最左边
        p -= 1
        n >>= 1
    return ans
# 时间复杂度和空间都是 O(1)

print(reverseBinary(1))