class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n= len(grid), len(grid[0])
        paths = [[ float('inf') for _ in range(n+1)] for _ in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                paths[i][j] = min(paths[i-1][j], paths[i][j-1]) + grid[i-1][j-1]
                paths[1][1] = grid[0][0]
        return paths[m][n]