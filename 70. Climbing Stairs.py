class Solution:
    def __init__(self):
        self.demo = {}
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in {1,2,3}:
            return n
        if n in self.demo:
            return self.demo[n]
        else:
            value = self.climbStairs(n-1) + self.climbStairs(n-2)
            self.demo[n] = value
            return  value