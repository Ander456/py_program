# -- coding: utf-8 --
# Using GroupBy Algorithm to Compress String
# 压缩字符串

# Given a string lowercase alphabet s, eliminate consecutive duplicate characters from the string and return it. That is, if a list contains repeated characters, they should be replaced with a single copy of the character. The order of the elements should not be changed.

# Constraints
# 0 ≤ n ≤ 100,000 where n is the length of s
# Example 1
# Input
# s = “aaaaaabbbccccaaaaddf”
# Output
# “abcadf”
# Example 2
# Input
# s = “a”
# Output
# “a”

# Try maintaining 2 pointers to remove the duplicates in place.

from itertools import groupby


def f(s):
    ans = []
    prev = None
    for i in s:
        if not prev or prev != i:
            ans.append(i)
        prev = i
    return "".join(ans)

def f2(s):
    return "".join(x for x,y in groupby(s))