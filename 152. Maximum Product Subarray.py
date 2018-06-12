class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum=big=small=nums[0]
        for n in nums[1:]:
            big, small=max(n, n*big, n*small), min(n, n*big, n*small)
            maximum=max(maximum, big)
        return maximum