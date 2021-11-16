# -- coding: utf-8 --
# Greedy Algorithm of Buying Cars
# 贪心算法 买车

def f(budget, prices):
    prices.sort() #这句很关键 我们要贪心每次都拿 最大或者最小的 那么排序就很重要了
    ans = 0
    for i in prices:
        if budget > i:
            budget -= i
            ans += 1
        else:
            break
    return ans


print(f(100, [10,30,15,45,20,8,35]))

# 时间复杂度是 排序O(nlogn) + O(n)  这样O(nlogn)更大 取它