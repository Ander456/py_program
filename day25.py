# -- coding: utf-8 --
# Enhanced Valid Parenthese String Algorithm using a Stack
# 用栈来解决 多种括号混合 来判断 括号是否合法问题

# 我们把左括号都推入栈 如果拿到的是右括号我们从栈里弹出一个元素来看是不是一对 不是则不合法

def f(s):
    st = []
    for i in s:
        if i in ["(", "[", "{"]:
            st.append(i)
        elif i in [")", "]", "}"]:
            if len(s) == 0 or (st[-1] + i not in ["()", "[]", "{}"]):
                return False
            st.pop()
    return len(st) == 0


print(f("(({{}}]]"))

print(f("(())[[]]{{()}}"))