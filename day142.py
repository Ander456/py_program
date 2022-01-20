# -- coding: utf-8 --
# Greedy Algorithm to Complete Tasks
# 用贪心算法 解决完成最大任务数量问题

# Example 1
# Input
# tasks = [3, 2, 9, 13]
# people = [10, 5, 2, 1]
# Output
# 3

# tasks是所有任务 以及需要的 体力 
# people 表示每个人的体力
# 求这些人能完成的最大的任务数量 

# 如果让10体力的人去做了2体力需求的任务 那么 就没人能完成9体力的活了 这肯定不合适 我们贪心的想每个人都完成自己最大限度的事那么肯定最贪心

def f(tasks, people):
    # 为了更好的贪心我们先排序
    tasks.sort()
    people.sort()
    ans = 0 # 最大可以完成的任务数量
    i = j = 0 # 双指针
    while j < len(tasks) and i < len(people):
        if people[i] >= tasks[j]:
            ans += 1
            i += 1
            j += 1
        else:
            i += 1
    return ans
# 时间复杂度 O(NlogN) 排序的时间

print(f([3,2,9,13], [10,5,2,1]))

