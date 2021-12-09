# -- coding: utf-8 --
# Python Function to Check If Valid IPv4 Address
# 检测一个ip地址是否是合法的 ipv4地址

# ipv4  有32位 4段每段8位 0-255 
# ipv6  有128位 是因为ipv4不够了世界上电脑太多 

def isValidIpv4(s):
    arr = s.split(".")
    if len(arr) != 4:
        return False
    for i in arr:
        # if not i.isnumeric():
        #     return False
        if int(i) < 0 or int(i) > 255:
            return False
        if int(i) == 0 and i != "0": # 00.0.0.0
            return False
    return True

print(isValidIpv4("1.1.1.1"))
print(isValidIpv4("1.1.1"))
print(isValidIpv4("1.1.1.1.1"))
print(isValidIpv4("256.1.1.1"))
print(isValidIpv4("00.1.1.1"))