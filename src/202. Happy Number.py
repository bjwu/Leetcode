class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        demo = set([n])
        return self._isHappy(n, n, demo)
    def _isHappy(self, n, num, demo):
        new = 0
        for i in str(n):
            new += int(i)**2
        # 这一句可以进行改进：## new = sum([int(i)**2 for i in str(n)])
        if new == 1:
            return True
        elif new in demo:
            return False
        else:
            demo.add(new)
            return self._isHappy(new, num, demo)
            