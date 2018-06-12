class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)//2+1):
            if nums[i] <= nums[-(i+1)]:
                return min(nums[i-1], nums[i], nums[-(i+1)], nums[-i])