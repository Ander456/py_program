# -- coding: utf-8 --
# Converting Spreadsheet Column Titles to Number
# excel单元格 给定一个 单元格 AB 返回这是第几列
# excel单元表格 从A开始到Z然后AA->xxx

# 这个和进制一样 比如 2进制 10进制 
# 10进制计算一个数 0*10+第一个数 + 这个数乘以10+第二个数 + xxx  比如123 = 0*10+1得1  然后1*10+2 得12 然后12乘以10+3 = 123
# 二进制同理 0*2+第一个数 + 这个数乘以2+第二个数   比如1110 = 0*2+1 得1 然后1*2+1 得 3 然后 3*2+1 得 7 然后 + 0 = 7

# 那么 A-Z义工26个字母 

def f(s):
    a = 0
    for i in s:
        a = a * 26 + (ord(i) - 65 + 1)  # A = 65
    return a
# 时间复杂度O(N)

print(f("AB"))