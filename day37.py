# -- coding: utf-8 --
# Hexadecimal Numbers Conversion
# 十六进制数转换
# 同day35 10进制也好 2进制也好 16进制也好 都是 我们用到的base的数的个数 
# 十六进制 0-9 A-F 一共16个 所以叫十六进制

# 十进制怎么转十六进制？ 同转二进制一样 一个数不断的除以16然后余数 最后到0位置 从下到上把余数连起来就是 二进制同理
# 十六进制怎么转十进制？ 同二进制转十进制一样 
# 我们求一个十进制数比如1234  1*10**3 + 2*10**2 + 3*10**1 + 4*10**0 
# 那么十六进制呢？ 比如FF （F=15) 15*16**1 + 15*16**0 = 240 + 15 = 255
# 那么二进制呢？ 比如 111      1*2**2 + 1*2**1 + 1*2**0 = 7


def dec2hex(s):
    mapping = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    ans = ""
    while s > 0 :
        ans = mapping[s % 16] + ans  # 对16取余可能有16种可能 所以要一个mapping 同理对2取余有两种 这里要是二进制就是 %2
        s //= 16
    return ans if ans != "" else "0"

print(dec2hex(255))

# 补充一哈 这里时间复杂度不是O(N) 而是O(log16为底的N) 通常二叉树那一类是O(log以二为底的N)（简略成了O(logN）

def hex2dec(h):
    ans = 0
    mapping = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15,        
    }
    for i in h:
        ans = ans * 16 + mapping[i.upper()]   # 这里和二进制是一样的 因为我们求十进制到二的时候是不断除以2余数reverse的  十六进制同理 所以返回去的时候要乘以16然后+作为余数的当前的i
    return ans 


print(hex2dec("FF"))


