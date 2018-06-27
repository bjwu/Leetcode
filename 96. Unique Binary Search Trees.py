class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = [1, 1] + [0]*(n-1)
        for i in range(2,n+1):
            for j in range(i):
                memo[i] += (memo[j]*memo[i-j-1])
        return memo[n]
                