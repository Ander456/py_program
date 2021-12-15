# -- coding: utf-8 --
# Introduction to Permutation and Combination
# 介绍了下 排列和组合

# If there are N items, we have N choices for the first item, and N-1 for the second item and so on. Thus:
# P(N,M) N个元素第M个的选择数 = N * (N - 1) * (N - 2) ... (N - M + 1) = N!/(N-M)!

# For Combination, the order does not matter. So we can first count the P(N, M) and then divide by P(M, M).
# 从n个不同的元素中，任取m（m≤n）个元素为一组，叫作从n个不同元素中取出m个元素的一个组合

# 举个例子 1，2，3三个数 排列 总数是 3!/(3-3)!  由于0！规定是1 那么得到就是 3x2x1 = 6种排列
# 1，2，3 这三个数 取出2个数为一组 有多少组？ 那就是6/2 = 3    P(3,2)/P(2,2) = (3!/1!)/(2!) = 3


# If we want to calculate C(N, M), for the last item, we can choose to pick or not pick. 
# If we pick, we have C(N-1, M-1), if we don’t pick the last item, then we have C(N-1, M). Therefore:
# C(N,M) = C(N-1,M-1) + C(N-1, M)

# caching the intermediate results
# @lru_cache(None)
def C(N, M):
  if M == N or M == 0:
    return 1
  if M == 1:
    return N
  return C(N - 1, M - 1) + C(N - 1, M) 

# 上线这个和day52的 三角形 算法 如此相同 真的好巧妙