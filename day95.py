# -- coding: utf-8 --
# Confusing Number Validation Algorithm
# 验证一个数是否是令人困惑的数 
# 啥意思呢 0 1 8 这仨数 你从上看和从下看 都是0 1 8  6呢会变成9 9会变成6 （其实就是旋转180度） 
# 而 2 3 4 5 7 这几个数从上和下看就明显能看出来了

# give a number N, return true if and only if it is a confusing number
def confusing(n):
    def turn(x):
        if x == 0 or x == 1 or x == 8:
            return x
        if x == 6:
            return 9
        if x == 9:
            return 6
        return -1 # 2 3 4 5 7
    n = str(n)
    ans = ""
    for i in n:
        x = turn(int(i))
        if x == -1:
            return False
        ans = str(x) + ans
    return n == ans

print(confusing(123)) 
print(confusing(8)) 