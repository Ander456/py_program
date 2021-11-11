# -- coding: utf-8 --
# Min Number of Brackets Needed to Make a Valid Parenthese String
# 给定一个只包含括号的字符串 求把这个字符串修复成 合法的 括号字符串 所需要的最小的括号数量
# 比如 ()) 需要（ 也就是1  ））） 需要3  

# 其实思想就是 如果碰到了(那么同day23我们balance+=1 如果都是(那么最后就补齐这么多个)就行
# 但是如果碰到了 ）那么我们需要记录一下 有多少个) 来决定补 blance + 记录的 括号 

# 其实结合day23 balance的作用是记录 ( 比 ) 的平衡度  等于0平衡才是合法的
# 只要<0那么久表示当前已经不合法了，那么如果要修复肯定就是记录一下这里不合法了也就是ans+=1
# 同理再次把balance重置为0 接着遍历 最终求我们balance（如果有数肯定是>=0）的也就是多出来的( 同理再加上需要修补的记录) 就是我们需要的数目

def f(s):
    balance, ans = 0,0 
    for i in s:
        if i == "(":
            balance += 1
        elif i == ")":
            balance -= 1
            if balance < 0:
                balance = 0
                ans += 1
    return ans + balance

print(f("((())"))
print(f(")))"))
print(f(")("))
print(f("()"))