class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        b = 0
        for c in nums:
            a, b = (a&~b&~c)|(~a&b&c), (~a&b&~c)|(~a&~b&c)
        return a|b