# -- coding: utf-8 --
# Compute the Intersection of the Intervals
# 计算给定的一组intervals 的 共同区域
# 比如 [1,5] [3,7] 那么他们的intersection交界部分就是 [3,5]
# 再比如 [1,5] [3, 7] [10, 100] 那他们就没有intersection 因为 第三个和前两个不相交

# The intersection, if there is any, must be formed by [left, right] 
# where left is the maximum of two starting points, and right is the minimal of two finishing points.

# 也就是说如果真的存在所有intervals有共同intersection那么肯定是 
# 左边的数肯定是所有区段的左数中最大的 而右是最小的 要不然肯定存在一个不共同区域

# intervals是[[a,a],[b,b]]格式的二维数组
def intervalsIntersection(intervals):
    if len(intervals) == 0:
        return None
    left = intervals[0][0] # startpoint
    right = intervals[0][1] # finishedpoint
    for i in intervals:
        left = max(left, i[0])
        right = min(right, i[1])
    if left > right:
        return None
    return [left, right]

print(intervalsIntersection([[1,5],[3, 7],[10, 100]]))    

print(intervalsIntersection([[1,5],[3, 7]]))   
