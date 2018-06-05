class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        
        n, m = len(obstacleGrid[0]), len(obstacleGrid)
        paths = [[0 for _ in range(n+1)] for _ in range(m+1)] 
        paths[1][1] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if obstacleGrid[i-1][j-1] == 1:
                    paths[i][j] = 0
                elif i != 1 or j != 1:
                    paths[i][j] = paths[i-1][j] + paths[i][j-1]
        return paths[m][n]