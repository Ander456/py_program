# -- coding: utf-8 --
# Perfect Number Validation Algorithm
# 检测一个数是否是 perfect number
# 比如28  = 1 + 2 + 4 + 7 + 14   而且 这些数字都可以被28整除 那么28就是一个 perfect number
# 到此我们接触了 happynumber 不断除最后是1 的  然后是 uglynumber 只能被2，3，5整除的  confusingnumber 上下看都一样的

def isPerfectNumber(n):
    if n <= 0:
        return False
    ans = 0
    for i in range(1, n//2 + 1):
        if n % i == 0:  #表示是divisor
            ans += i
            if ans > n:
                return False
    return ans == n
# 时间复杂度O(N)
print(isPerfectNumber(28))
print(isPerfectNumber(14))

# 我们看到的规律是 28 有1的时候一定有28  有2的时候有14  有4的时候有7 也就是有一个除数同时就得有一个 n/这个除数的除数 才有可能是perfect number
def isPerfectNumber2(n):
    if n <= 0:
        return False
    i, s = 1, 0
    while i * i <= n:
        if n % i == 0:
            s += i
            if i * i != n: # 啥意思呢 16这个数字 4是它的除数 16/4还是4 不能加重复的
                s += n//i  
        i += 1
    return s == n + n  #因为我们当i==1时候 s+=28/1 多加了一个 n 
# 时间复杂度O(根号N) 比上面的方法效率高

print(isPerfectNumber2(28))