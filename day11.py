# -- coding: utf-8 --
# Compute the Sum of the Digits using Three Methods
# 计算进制各个位的和

# 123 => 6  from :1 + 2 + 3

def numOfDigits(n):
    s = str(n)
    ans = 0
    for i in s:
        ans += int(i)
    return ans


print(numOfDigits(123))


def numOfDigits2(n):
    ans = 0
    while n > 0:
        ans += n % 10
        n = n // 10
    return ans


print(numOfDigits2(123))


# 递归
def numOfDigits3(n):
    #要递归就得有base-case终止条件
    if n == 0:
        return 0
    return n % 10 + numOfDigits3(n // 10)


print(numOfDigits3(123))