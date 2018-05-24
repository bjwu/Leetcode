class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        import math
        return int(math.sqrt(x))

# 对单个数的运算，math库比numpy要快
# 而对于数组的数学运算，则相反