"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？
"""

# 转移方程,m和n为坐标
# f(m,n) = f(m-1,n) + f(m,n-1)
# 从小到大的动态规划，应该没有更好的办法了吧

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[1] * m] + [[1] + [0] * (m-1)] * (n-1)
        for i in range(1, n):
            for j in range(1, m):
                memo[i][j] = memo[i-1][j] + memo[i][j-1]
        return memo[n-1][m-1]