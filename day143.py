# -- coding: utf-8 --
# Using Heap (Priority Queue) to Generate Nth Ugly Number
# 用堆来计算 第n个 ugly number
# ugly number 参考 day90 . Ugly number is a positive number whose prime factors only include 2, 3, and/or 5.

# Example 1:
# Input: n = 10
# Output: 12
# Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.

# Example 2:
# Input: n = 1
# Output: 1
# Explanation: 1 is typically treated as an ugly number.

from heapq import heappop, heappush

def nthUglyNumber(n):
    seen = set([1])
    heap = [1]
    for _ in range(n):       # O(N)
        cur = heappop(heap)  # 这样的操作是O(1))
        for i in [2,3,5]:
            val = cur * i
            if val not in seen:
                seen.add(val)
                heappush(heap, val) #这个操作不频繁 O(LogN)
    return cur 

# The time complexity will thus be roughly O(N) and the space complexity is O(N) as we are using hash set

# 思想就是
# We can keep the ugly numbers in a heap (or priority queue), then for next ugly number, we pick the smallest ugly number that we have generated so far, 
# and multiply another prime factor of 2, 3, and 5, and if it has not been seen, we push it back to the priority queue (or insert it into the heap).
# 只有它本身是个丑数 那么他作为因子factor  2,3,5才会还是丑数