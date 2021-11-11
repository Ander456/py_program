# -- coding: utf-8 --
# Check a Valid Parenthese String
# 检测给定字符串括号是否是合法的

# Parenthese ()   # bracket []  # curve {}

# 合法括号必须是 以( 开头 )结尾  并且总数量是偶数
# 其实就是定义一个balance 碰到（就增 碰到)就减
def f(s):
    balacne = 0
    for i in s:
        if i == "(":
            balacne += 1
        elif i == ")":
            balacne -=1
            if balacne < 0:
                return False
    return True


print(f("((()))"))
print(f(")((()))"))
print(f(")((()))"))