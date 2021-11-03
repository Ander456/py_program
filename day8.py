# -- coding: utf-8 --
# Different Algorithms to Check if a String is Palindrome
# 检测是否是回文串

def isPalindrome(s):
    return rev(s) == s

def rev(s):
    return s[::-1]

def rev2(s):
    ans = ""
    for i in s:
        ans = i + ans
    return ans

print(isPalindrome("abcdcba"))

# 双指针法
def isPalindrome2(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


print(isPalindrome2("abcdcba1"))


# Remember the data structure Stack – which is First In Last Out. We can convert the string into a list and use it as a stack – pop one element and check if the corresponding letter (from the begining) is the same:
def isPalindrome3(s):
    arr = list(s)
    for i in s:
        x = arr.pop()
        if x != i:
            return False
    return True


print(isPalindrome3("abcdcba"))