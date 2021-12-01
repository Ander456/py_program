# -- coding: utf-8 --
# Re-implement the enumerate in Python using yield in a Generator
# 重新实现 pyton中的 enumerate
# enumerate 返回 i和对应的val

def my_enumerate(n):
    for i in range(len(n)):
        yield (i, n[i])

s = "Hello!"
for i, v in my_enumerate(s):
    print(i, v)