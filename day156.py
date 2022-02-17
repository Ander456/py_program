# -- coding: utf-8 --
# Hour and Minute Angle on a Clock
# 时针和分针的角度计算

# Constraints
# 0 ≤ hour ≤ 23
# 0 ≤ minutes ≤ 59
# Example 1
# Input
# hour = 12
# minutes = 22
# Output
# 121
# Remember to take the angle displaced by the hour hand due to movement by minute hand (Try to make floating type calculations).
# if the angle is > 180 , return 360-angle

from math import floor


def f(hour, minute):
    hour %= 12
    hh = (hour + minute / 60) * 30  # 一小时是30度 然后 + 分钟给的hour度偏移
    mm = minute * 6
    ang = abs(hh - mm)
    return floor(min(ang, 360 - ang))

print(f(12,22))