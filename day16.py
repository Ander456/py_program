# -- coding: utf-8 --
# Solving the Jump Game by Depth First Search Algorithm
# 通过 dfs 来解决昨天的跳格子游戏
# 比如给定一列数 [2,0,3,1,3,4] 起点索引是3那就是在1的位置上 表示我们可以向左或者向右走1步 
# 之后如果我们选择向右那么 就站在了索引是4的位置上也就是 3 表示我们此时可以向左或者向右走3步 我们的目标数走到0那里
# 问我们是否可以根据给定的数和起点走到目标位置0
# ps 超过数列边界的可以抛弃

def dfs(n, s, nb):
    if n[s] == 0:
        return True
    for i in [-1, 1]:
        # 这时我们又两个选择
        next = s + i * n[s]
        if next < len(n) and next >= 0 and (next not in nb):
            nb.add(next)
            # 给notebook添加了之后我们要继续往深走 自然而然就是递归
            if dfs(n, next, nb):
                # 表示说如果我这次选择可以走到目标位置
                # nb.remove(next)
                return True
            nb.remove(next) # 这里为什么要删掉从notebook里就是我们上次选择不对那么那些我们标记的要被取消调因为我这次选择很可能再去找这些
    return False # 如果都没找到表示不行


print(dfs([4,2,3,0,3,1,2], 0, set()))

print(dfs([4,2,3,0,3,1,2], 1, set()))
