# -- coding: utf-8 --
# Minimum Cost to Connect Sticks (Priority Queue/Min Heap)
# 最小的cost来连接木棍

# You have some number of sticks(棍子) with positive integer lengths. 
# These lengths are given as an array sticks, where sticks[i] is the length of the ith stick. 
# You can connect any two sticks of lengths x and y into one stick by paying a cost of x + y. 
# You must connect all the sticks until there is only one stick remaining.
# Return the minimum cost of connecting all the given sticks into one stick in this way.

# 连接木棍的消耗 x+y 你其实可以想象成 举起来需要消耗的能量 我们肯定想找消耗能量最小的方案 ps：放下不消耗能量
# 比如 1，2，3 三个木棍
# 如果我们 先举起 1 和 2 来连接 那么消耗3 放下 然后 再举起 3 和 剩下的3 那么消耗 6 那么两次一共消耗 3 + 6 = 9
# 如果我们 先举起 2 和 3 那么消耗 5  放下 然后再举起这个5 和剩下的1 消耗 6  那么两次一共消耗能 5 + 6 = 11


# 我们可以看出 每次我们都举起最小的两个来那么一定消耗最小 一提到每次都最小 那肯定是min heap

import heapq as hq

def connectSticks(s):
    hq.heapify(s)
    cost = 0
    while len(s) > 1: #最后只剩一根
        x, y = hq.heappop(s), hq.heappop(s)
        cost += x + y
        hq.heappush(s, x + y)
    return cost

print(connectSticks([1,2,3]))