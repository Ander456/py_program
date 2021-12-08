# -- coding: utf-8 --
# Add One to List
# 列表+1
# [1,2,3] + 1 = [1,2,4]
# [9,9] + 1 = [1,0,0]
# 这和day69的 两个链表相加 相似 都需要 一个 进位的carry

def addOneToList(nums):
    carry = 0
    n = len(nums) - 1
    nums[-1] += 1 # -1就是最后一个 python太牛逼了
    while n >= 0:
        nums[n] += carry
        carry = nums[n] // 10
        nums[n] %= 10
        # if nums[n] == 0:
        #     break
        n -= 1
    if carry > 0:
        nums.insert(0, carry)
    return nums

print(addOneToList([1,2,3]))

print(addOneToList([9,9]))

print(addOneToList([1,0,9]))
