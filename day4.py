# Reversing a List using Stack
# Stack frist in last out
# 栈结构先进后出

def rev(nums):
    ans = []
    while len(nums) > 0:
        x = nums.pop()
        ans.append(x)
    return ans


print(rev([1,2,3,6]))