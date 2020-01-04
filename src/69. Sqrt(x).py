"""
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
"""

# 具体看二分法模版
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, max(x, 1)
        while (left < right):
            mid = left + (right - left + 1) // 2
            if mid * mid <= x:
                left = mid
            else:
                right = mid - 1