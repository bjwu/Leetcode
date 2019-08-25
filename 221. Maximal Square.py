class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        matrix = [list(map(int, m)) for m in matrix]
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][j]:
                    matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
        return max([max(i) for i in matrix])**2