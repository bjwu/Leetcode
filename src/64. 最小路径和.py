"""
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 直接从原数组上面改就行
        # 遍历第一行
        for j in range(1, len(grid[0])):
            grid[0][j] = grid[0][j - 1] + grid[0][j]

        # 遍历第一列
        for i in range(1, len(grid)):
            grid[i][0] = grid[i - 1][0] + grid[i][0]

        # 遍历剩余矩阵
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                grid[i][j] = grid[i][j] + min(grid[i][j - 1], grid[i - 1][j])

        return grid[-1][-1]

# 其实我觉得我的办法已经是最好的办法了，二维动态规划，且储存为O(1)，因为使用原数组进行储存
# 但是不知为何超过率却异常的低