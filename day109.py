# -- coding: utf-8 --
# Using a Stack to Remove All Adjacent Duplicates In String
# 使用堆栈来移除相邻相同字符的算法

# Input: “abbaca” Output: “ca”
# 因为bb是 移除掉 然后aa连着了 删除掉 剩下ca

def f(s):
    for i in range(1, len(s)):
        # 从第2个字母开始到最后一个
        if s[i] == s[i-1]:
            return f(s[:i-1] + s[i+1:]) # 把i 和 i-1 这俩移除掉
    return s
# 时间复杂度O(N平方) 因为每次递归进去都要 for循环1-N
print(f("abbaca"))


def f2(s):
    st = [] # stack
    for i in s:
        if len(st) != 0 and i == st[-1]: #表明当前拿到的i和栈顶一样 那么pop
            st.pop()
        else:
            st.append(i)
    return ''.join(st)
# 时间复杂度O(N)  空间复杂度O(N)
print(f2("abbaca"))