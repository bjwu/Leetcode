class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for i in range(1, len(triangle)):
            triangle[i][0] += triangle[i-1][0]
            for j in range(1, i):
                triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
            triangle[i][i] += triangle[i-1][i-1]
        return min(triangle[-1])