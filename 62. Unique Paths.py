class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """ 
        # 这是自顶向下的DP，当然时间超了
        # if m == 1 or n == 1:
        #     return 1 
        # else:
        #     return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
        
        # 一下是bottom-up法，明显快很多
        ## 话说，对于list的零矩阵初始化可以这样写，哈哈
        paths = [[0 for _ in range(n+1)] for _ in range(m+1)] 
        for i in range(1,m+1):
            for j in range(1,n+1):
                paths[i][j] = paths[i-1][j] + paths[i][j-1]
                paths[1][1] = 1
        return paths[m][n]