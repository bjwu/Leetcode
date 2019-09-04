"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
"""

# 跟62题同样的办法，只不过遇到obstacle的时候把相应的memo位置置为0即可
# 但是初始值可能需要改变，因为obstacle可能会在初始值的位置

# 以下方法的遍历采用在数组外包了一层0层来遍历
# 其实还可以先遍历第一行和第一列，剩下的在根据转移方程进行遍历

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # n, m = rows, columns
        if obstacleGrid[0][0] == 1:
            return 0
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        memo = [[0] * (m+1)] * (n+1)
        memo[1][1] = 1
        for i in range(1, n+1):
            for j in range(1, m+1):
                if obstacleGrid[i-1][j-1] == 1:
                    memo[i][j] = 0
                else:
                    memo[i][j] = memo[i-1][j] + memo[i][j-1]
        return memo[n][m]

# 时间复杂：O(M*N)
# 空间复杂：O(M*N)
# 其实可以直接利用obstacleGrid这个数组来储存，这样空间复杂度就不需要了