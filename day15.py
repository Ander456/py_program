# -- coding: utf-8 --
# Revisit Breadth First Search Algorithm via Jump Game
# 通过跳步游戏复习 bfs算法
# 比如给定一列数 [2,0,3,1,3,4] 起点索引是3那就是在1的位置上 表示我们可以向左或者向右走1步 
# 之后如果我们选择向右那么 就站在了索引是4的位置上也就是 3 表示我们此时可以向左或者向右走3步 我们的目标数走到0那里
# 问我们是否可以根据给定的数和起点走到目标位置0
# ps 超过数列边界的可以抛弃

def bfs(nums, s):
    if len(nums) == 0:
        return False
    seen = set()
    q = [s]
    while len(q) > 0:
        index = q.pop(0)
        # base case也就是终止条件
        if nums[index] == 0:
            return True
        for i in [-1, 1]: #因为可以选择左或者右
            next = index + i * nums[index]
            if next not in seen and next >= 0 and next < len(nums):
                q.append(next)
                seen.add(next)
    return False


print(bfs([2,0,3,1,3,4], 3))

print(bfs([1,0,1,5,8,9], 5))
