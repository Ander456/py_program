# -- coding: utf-8 --
# Compute the Number of Set Bits in an Integer
# 计算一个十进制数的 二进制里有多少位1

# 比如 8 - 1000 有1个1
# 5 - 101  有2个1

def numsOfOneInBits(n):
    ans = 0
    while n > 0:
        ans += n & 1 # 与上1 如果最右位是1 那么结果是1 如果最右位是0 那么结果为0
        n >>= 1 # shift 1位
    return ans

print(numsOfOneInBits(8))
print(numsOfOneInBits(5))
# 时间复杂度 O(1) 但是如果n无限大 时间复杂度是 O(log(N)) 因为一个十进制数的二进制的位数是 2的幂次 

# 通过day75我们知道 n & (n-1) 在二进制里是一个很有用的东西
# 不光可以判断是否是2的幂 也可以 变相的 消去 n最右位的1 
# 比如 9 1001 9-1 8 1000 与上 结果是 1000 这不就把最右的1消去了么
# 只要这个数是2的幂 那么它肯定是一个1跟着n个0
def numsOfOneInBits2(n):
    ans = 0
    while n > 0:
        ans += 1  # 每要与一次 就+1个 表示我们消去了一个1
        n = n & (n - 1)
    return ans

print(numsOfOneInBits2(5))
print(numsOfOneInBits2(8))


# 当然python也有bin操作
def numsOfOneInBits3(n):
    b = bin(n)
    ans = 0
    for i in b:
        if i == "1":
            ans += 1
    return ans

print(numsOfOneInBits3(5))
print(numsOfOneInBits3(8))