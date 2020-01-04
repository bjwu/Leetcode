"""
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
"""

# 自顶向下
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 首先遍历最左边和最右边
        for i in range(1, len(triangle)):
            triangle[i][0] += triangle[i-1][0]
            triangle[i][-1] += triangle[i-1][-1]
        # 其次遍历中间值
        for i in range(2, len(triangle)):
            for m in range(1, i):
                triangle[i][m] += min(triangle[i-1][m-1], triangle[i-1][m])
        return min(triangle[-1])

# 如果是自底向上的话则不需要考虑边界问题
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle)-2, -1, -1):
            for m in range(i+1):
                triangle[i][m] += min(triangle[i+1][m], triangle[i+1][m+1])
        return triangle[0][0]