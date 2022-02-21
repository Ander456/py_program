# -- coding: utf-8 --
# Remove Vowels from a String
# 删除字符串中的元音字符的算法

# Example 1:
# Input: s = “leetcodeisacommunityforcoders”
# Output: “ltcdscmmntyfrcdrs”

# Example 2:
# Input: s = “aeiou”
# Output: “”

# Constraints:
# 1 <= s.length <= 1000
# s consists of only lowercase English letters.

# How to erase vowels in a string?
# Loop over the string and check every character, if it is a vowel ignore it otherwise add it to the answer.

def f(s):
    ans = []
    for i in s:
        if i not in "aeiou":
            ans.append(i)
    return "".join(ans)

def f2(s):
    ans = []
    vowels = set("aeiou")
    for i in s:
        if i not in vowels:
            ans.append(i)
    return "".join(ans)

def f3(s):
    return "".join([c for c in s if c not in "aeiou"])

def f4(s):
    return "".join(filter(lambda x:x not in "aeiou", s))