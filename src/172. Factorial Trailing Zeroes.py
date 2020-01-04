class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 0 if n == 0 else n // 5 + self.trailingZeroes(n // 5)

# Because all trailing 0 is from factors 5 * 2.

# But sometimes one number may have several 5 factors, for example, 25 have two 5 factors, 125 have three 5 factors. In the n! operation, factors 2 is always ample. So we just count how many 5 factors in all number from 1 to n.

# 所以说，这个题目所有的0都是由于5提供的。所以每隔5个数有一个5，每隔5*5个数有两个5，每隔5*5*5个数有3个5...

# ```py
# return 0 if n == 0 else n // 5 + self.trailingZeroes(n // 5)
# ```