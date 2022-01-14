# -- coding: utf-8 --
# Packing Boxes Algorithm using GroupBy
# 打包  比如 给定 [111,22,3,44] 结果 [[1,1,1], [2,2], [3], [4,4]]

# 我们给定一个 ans最终[] 给一个 cur当前打包盒子 然后 不断判断当前指针指着的数是否能放到当前curbox 如果可以就放 如果不是一样的数了 那么 当前结果box放到最终大ans里

from itertools import groupby


def f(nums):
    ans = []
    cur = []
    prev = None
    for i in range(nums):
        if i == prev:
            cur.append(i)
        else:
            if cur:
                ans.append(cur)
            cur = [i] # 放入新的盒子相当于
        prev = i
    if cur:
        ans.append(cur) # 看最后的当前盒子是否还有东西 如果有 直接塞到最终结果里
    return ans

# 时间复杂度O(N) 空间同

def f2(nums):
    return [list(y) for x, y in groupby(nums)]  # make an iterator that returns consecutive keys and groups from the iterable